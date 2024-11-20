from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and updating blog posts"""

    class Meta:
        model = Post
        fields = ["title", "content", "excerpt", "image", "image_alt", "status"]
        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 5}),
            "content": TinyMCE(),
        }

        labels = {
            "title": "Post Title",
            "content": "Content",
            "excerpt": "Excerpt",
            "image": "Image",
            "image_alt": "Describe Image",
            "status": "Save as Draft or Publish",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
