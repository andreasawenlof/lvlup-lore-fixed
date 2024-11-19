from django.urls import path
from .views import PostList, PostDetail, CreatePost

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("post_detail/", PostDetail.as_view(), name="post_detail"),
    path("post/new", CreatePost.as_view(), name="create_post"),
]
