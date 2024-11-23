""" Import the necessary modules """
from django.db.models import Q, Count
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostList(ListView):
    """ List of all posts """
    template_name = "blog/index.html"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = self.annotate_comment_count(Post.objects.filter(status=1))

        # If there's a search query, filter posts by title
        if query:
            return queryset.filter(Q(title__icontains=query)).order_by("-created_on")

        # If no query is provided, show all posts
        return queryset.order_by("-created_on")

    def annotate_comment_count(self, queryset):
        """ Annotate the queryset with the number of comments on each post """
        return queryset.annotate(comment_count=Count("comments"))


class DraftPostList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ List of all draft posts """
    template_name = "blog/draft_posts.html"
    model = Post
    context_object_name = "drafts"
    paginate_by = 3

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


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = 1  # Assuming 1 is the status for published
    post.save()
    # Redirect to the draft posts page or any other page
    return redirect('draft_posts')


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
        return self.request.user.is_staff


def edit_comment(request, slug, comment_id):
    """ view to edit a comment """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        # Update the comment body
        comment.body = request.POST.get("body")
        comment.save()
        messages.success(request, "Comment updated successfully!")
        return redirect("post_detail_by_slug", slug=slug)

    messages.error(request, "Invalid request.")
    return redirect("post_detail_by_slug", slug=slug)


def delete_comment(request, slug, comment_id):
    """ view to delete a comment """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(request, messages.ERROR,
                             "You can only delete your own comments!")

    return HttpResponseRedirect(reverse('post_detail_by_slug', args=[slug]))
