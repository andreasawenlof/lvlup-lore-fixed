from django.contrib import admin
from django.db import models
from .models import Post, Comment
from django.contrib.admin import ModelAdmin
from tinymce.widgets import TinyMCE


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """Admin interface for managing Posts"""

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
    formfield_overrides = {
        models.TextField: {
            "content": {"widget": TinyMCE()},
        },
    }

    # list_display = ("title", "slug", "author", "created_on", "status")
    # list_filter = ("status", "created_on")


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    """Admin Interface for managing comments"""
