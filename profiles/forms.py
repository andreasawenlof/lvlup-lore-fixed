"""Forms for the profiles app"""
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to create a profile"""

    class Meta:
        """Meta class for the ProfileForm class"""
        model = Profile
        fields = ["image", "bio"]

        labels = {"image": "Avatar", "bio": "Bio"}
