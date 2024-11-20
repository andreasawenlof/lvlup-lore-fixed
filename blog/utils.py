from django.utils.text import slugify


def generate_unique_slug(model, title):
    """Generate unique slug for the model."""
    slug = slugify(title)
    unique_slug = slug
    extension = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{extension}"
        extension += 1
    return unique_slug
