""" This module defines the views for the contact form. """
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404

from .forms import ContactForm
from .models import Contact


def contact_view(request):
    """ View to handle the contact form """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your message has been sent. Thank you for contacting us. We'll get back to you shortly.",
            )
            # Redirect to the same page or another page after form submission
            return redirect("contact")
        else:
            return render(request, "contact/contact_form.html", {'form': contact_form})
    else:
        contact_form = ContactForm()
        return render(request, "contact/contact_form.html", {'form': contact_form})


def is_admin(user):
    """ Function to check if a user is an admin """
    return user.is_staff


@login_required
@user_passes_test(is_admin)
def contact_messages_view(request):
    """ View to display all contact messages """
    contacts = Contact.objects.all()
    return render(request, 'contact/contact_messages.html', {'contacts': contacts})


@login_required
@user_passes_test(is_admin)
def contact_message_detail_view(request, pk):
    """ View to display a single contact message """
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.read = not contact.read
        contact.save()
        return redirect('contact_message_detail', pk=pk)
    return render(request, 'contact/contact_message_detail.html', {'contact': contact})


@login_required
@user_passes_test(is_admin)
def contact_toggle_read_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.read = not contact.read
    contact.save()
    return redirect('contact_messages')
