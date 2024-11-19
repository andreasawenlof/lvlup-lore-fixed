from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")


class PostDetail(ListView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.filter(status=1)


class CreatePost(CreateView):
    """Create Post View"""

    template_name = "blog/create_post.html"
    model = Post
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)
