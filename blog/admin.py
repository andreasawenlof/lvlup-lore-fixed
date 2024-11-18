from django.contrib import admin
from .models import Post, Comment
from django.contrib.admin import ModelAdmin


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """Admin interface for managing Posts"""

    # list_display = ("title", "slug", "author", "created_on", "status")
    # list_filter = ("status", "created_on")


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    " Admin Interface for managing comments " ""
