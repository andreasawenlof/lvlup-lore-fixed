from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from .forms import ProfileForm
from .models import Profile
from blog.models import Post, Comment

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        user = User.objects.get(id=self.kwargs["pk"])
        profile = Profile.objects.get(user=user)

        # Get all posts that the user has commented on
        commented_posts = Post.objects.filter(comments__author=user).distinct()

        context = {
            "profile": profile,
            "commented_posts": commented_posts,  # Add the posts to the context
        }

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Profile View"""

    template_name = "profiles/edit_profile.html"
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.success_url = f"/profile/view/{self.kwargs['pk']}"
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_pbject().user
