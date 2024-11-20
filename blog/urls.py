from django.urls import path
from .views import PostList, post_detail, CreatePost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("<slug:slug>/", post_detail, name="post_detail"),
    path("post/new", CreatePost.as_view(), name="create_post"),
]
