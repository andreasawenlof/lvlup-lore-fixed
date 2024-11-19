from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostList(ListView):
    template_name = "blog/index.html"
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    context_object_name = "posts"


class PostDetail(ListView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.filter(status=1)


class CreatePost(LoginRequiredMixin, CreateView):
    """Create Post View"""

    template_name = "blog/create_post.html"
    model = Post
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)
