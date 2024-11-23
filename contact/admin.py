"""This module contains the admin configuration for the contact app."""
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Admin configuration for the Contact model """
    list_display = ('name', 'subject', 'message', 'read', 'created_on')
    readonly_fields = ('name', 'subject', 'email', 'message', 'created_on',)

    class Meta:
        """ Meta class for the ContactAdmin class """
        model = Contact
        fields = ['name', 'email', 'message', 'read']
