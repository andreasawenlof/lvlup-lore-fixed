from django.contrib import admin
from .models import Post
from django.contrib.admin import ModelAdmin


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """Admin interface for managing Posts"""

    list_display = ("title", "slug", "author", "created_on", "status")
