from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
