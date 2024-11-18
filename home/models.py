from django.db import models
from django.contrib.auth import user_logged_in


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
