from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    template_name = "home/index.html"
    queryset = Post.objects.filter(status=1)
