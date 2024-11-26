""" Import the necessary modules """

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from blog.models import Post

from .forms import ProfileForm
from .models import Profile


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, id=self.kwargs["pk"])
        profile = get_object_or_404(Profile, user=user)

        # Get all posts that the user has commented on
        commented_posts = Post.objects.filter(comments__author=user).distinct()

        context = {
            "profile": profile,
            "commented_posts": commented_posts,
            'form': ProfileForm(instance=profile)
        }

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Profile View"""

    template_name = "profiles/edit_profile.html"
    model = Profile
    form_class = ProfileForm

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Profile updated successfully")
        self.success_url = f"/profile/view/{self.kwargs['pk']}"
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error updating your profile. Please try again.")
        return super().form_invalid(form)
