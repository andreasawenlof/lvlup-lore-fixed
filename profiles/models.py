""" Import the necessary modules """

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField(
        "image", default="placeholder", blank=False, null=False)
    bio = models.TextField(max_length=2500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_user_profile(
    sender, instance, created, **kwargs
):  # pylint: disable=unused-argument
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)  # pylint: disable=no-member
    instance.profile.save()
