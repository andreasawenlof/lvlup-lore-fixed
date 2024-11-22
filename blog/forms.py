from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and updating blog posts"""

    class Meta:
        model = Post
        fields = ["title", "content", "excerpt", "image", "image_alt", "status"]
        widgets = {
            "content": TinyMCE(),  # Use TinyMCE for the `content` field
            "excerpt": forms.Textarea(
                attrs={"rows": 5}
            ),  # Standard Textarea for `excerpt`
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


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
