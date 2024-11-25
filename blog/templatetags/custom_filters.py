""" Custom template filters for the blog app """
# your_app/templatetags/custom_filters.py
from django import template
from django.utils import timezone
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def custom_timesince(value):
    """ Custom template filter to display human-readable time since """
    now = timezone.now()
    diff = now - value

    if diff.days > 0:
        return f"{diff.days} days ago"
    elif diff.seconds >= 3600:
        hours = diff.seconds // 3600
        return f"{hours} hours ago"
    elif diff.seconds >= 60:
        minutes = diff.seconds // 60
        return f"{minutes} minutes ago"
    else:
        return f"{diff.seconds} seconds ago"
