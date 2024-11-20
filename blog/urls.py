from django.urls import path
from .views import PostList, post_detail, CreatePost, EditPost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("post/<slug:slug>/", post_detail, name="post_detail"),
    path("post/new", CreatePost.as_view(), name="post_create"),
    path("post/<slug:slug>/edit/", EditPost.as_view(), name="post_edit"),
]
