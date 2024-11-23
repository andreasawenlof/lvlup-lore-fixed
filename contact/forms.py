""" This file contains the form for the contact page. """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form to handle contact form submissions """
    class Meta:
        """ Meta class for the ContactForm class """
        model = Contact
        fields = ['name', 'email', 'message']
