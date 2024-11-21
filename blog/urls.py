from django.urls import path
from .views import (
    PostList,
    post_detail,
    CreatePost,
    EditPost,
    DeletePost,
    DraftPostList,
)

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail_by_pk"),
    path("post/<slug:slug>/", post_detail, name="post_detail_by_slug"),
    path("post/create", CreatePost.as_view(), name="post_create"),
    path("post/<slug:slug>/edit/", EditPost.as_view(), name="post_edit"),
    path(
        "post/<slug:slug>/post_delete/<int:pk>/",
        DeletePost.as_view(),
        name="post_delete",
    ),
    path("drafts/", DraftPostList.as_view(), name="draft_posts"),
]
