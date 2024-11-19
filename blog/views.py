from django.views.generic import TemplateView, ListView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")


class PostDetail(ListView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.filter(status=1)
