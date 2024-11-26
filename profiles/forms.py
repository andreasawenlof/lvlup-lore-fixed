"""Forms for the profiles app"""
from django import forms
from tinymce.widgets import TinyMCE
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""

    class Meta:
        """Meta class for the ProfileForm class"""
        model = Profile
        fields = ["image", "bio"]
        widgets = {
            "bio": TinyMCE()
        }

        labels = {"image": "Avatar", "bio": "Bio"}
