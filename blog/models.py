""" Import the necessary modules """

from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from .utils import generate_unique_slug

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Defining Post Model"""

    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        editable=False,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        editable=False,
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    excerpt = models.TextField(blank=False, null=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="blog/images",
        force_format="WEBP",
        default="images/logo/logo6.webp",
        blank=False,
        null=False,
        max_length=100,
    )
    image_alt = models.CharField(
        max_length=100, null=False, blank=False, default="Describe the image"
    )
    status = models.IntegerField(choices=STATUS, default=0)

    objects = models.Manager()

    class Meta:
        """Meta class for ordering the posts"""

        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        # Generate slug if it's not set
        if not self.slug:
            self.slug = generate_unique_slug(Post, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    """Defining Comment Model"""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", editable=False
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", editable=False
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        """Meta class for ordering the comments"""

        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment on post with title: {self.post} | from {self.author}."
