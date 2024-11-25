""" This module contains the Contact model. """
from django.db import models


class Contact(models.Model):
    """ Model to store contact form submissions """
    subject = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f"Message with subject {self.subject}"
