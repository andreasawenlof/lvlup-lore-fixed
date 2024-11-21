from django.views.generic import TemplateView, UpdateView
from .forms import ProfileForm
from .models import Profile

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            "profile": profile,
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
