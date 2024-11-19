from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Defining Post Model"""

    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=False)
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

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment on post with title: {self.post.title} | from {self.author}."
