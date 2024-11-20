from django.contrib import admin
from django.db import models
from .models import Post, Comment
from django.contrib.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from .forms import PostForm


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """Admin interface for managing Posts"""

    form = PostForm
    list_display = (
        "title",
        "slug",
        "author",
        "excerpt",
        "created_on",
        "image",
        "image_alt",
        "status",
    )

    # list_display = ("title", "slug", "author", "created_on", "status")
    # list_filter = ("status", "created_on")


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    """Admin Interface for managing comments"""
