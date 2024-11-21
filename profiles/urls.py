from django.urls import path
from .views import Profiles

urlpatterns = [
    path("user/<int:pk>/", Profiles.as_view(), name="profile"),
]
