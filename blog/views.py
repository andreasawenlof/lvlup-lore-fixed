import logging
from django.db.models import Q, Count
from django.db.models.functions import Random
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm, EditCommentForm
from django.contrib import messages
from django.http import Http404, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostList(ListView):
    template_name = "blog/index.html"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = self.annotate_comment_count(Post.objects.filter(status=1))

        # If there's a search query, filter posts by title
        if query:
            return queryset.filter(Q(title__icontains=query)).order_by("-created_on")

        # If the search form was submitted with an empty query (active query but blank input)
        if self.request.GET.get("q") == "":
            return queryset.order_by(Random())[:1]

        # If no query is provided, show all posts
        return queryset.order_by("-created_on")

    def annotate_comment_count(self, queryset):
        return queryset.annotate(comment_count=Count("comments"))


class DraftPostList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "blog/draft_posts.html"
    model = Post
    context_object_name = "drafts"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status=0, author=self.request.user).order_by(
            "-created_on"
        )

    def test_func(self):
        return self.request.user.is_staff


def post_detail(request, pk=None, slug=None):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    if pk:
        post = get_object_or_404(Post, pk=pk)

    elif slug:
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

    else:
        raise Http404("Post does not exist")

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect("post_detail_by_slug", slug=post.slug)

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


class CreatePost(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Create Post View"""

    template_name = "blog/create_post.html"
    model = Post
    form_class = PostForm
    success_url = "/"

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a post"""

    template_name = "blog/edit_post.html"
    model = Post
    form_class = PostForm

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(EditPost, self).get_context_data(**kwargs)
        context["post"] = self.get_object()
        return context

    def get_success_url(self):
        post = self.object
        if post.status == 0:
            return reverse_lazy("post_detail_by_pk", kwargs={"pk": post.pk})
        else:
            return reverse_lazy("post_detail_by_slug", kwargs={"slug": post.slug})


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a Post"""

    model = Post
    success_url = reverse_lazy("home")

    def test_func(self):
        post = self.get_object()
        return self.request.user.is_staff


logger = logging.getLogger(__name__)


class EditComment(View):
    def post(self, request, pk):
        try:
            comment = get_object_or_404(Comment, pk=pk)
            if request.user == comment.author or request.user.is_staff:
                form = EditCommentForm(request.POST, instance=comment)
                if form.is_valid():
                    form.save()
                    if request.headers.get("x-requested-with") == "XMLHttpRequest":
                        return JsonResponse({"success": True, "body": comment.body})
                    else:
                        messages.success(
                            request, "Comment has been successfully updated."
                        )
                        return redirect("post_detail_by_slug", slug=comment.post.slug)
                else:
                    logger.error("Form is not valid: %s", form.errors)
            else:
                logger.error("User is not authorized to edit this comment")
        except Exception as e:
            logger.exception("An error occurred while editing the comment")

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"success": False, "error": "An error occurred"})
        return redirect("post_detail_by_slug", slug=comment.post.slug)
