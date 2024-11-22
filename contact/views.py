from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            if form.is_valid():
                # For now, print the form data to the console
                print(form.cleaned_data)
                # Redirect to success page
                return redirect(
                    "success"
                )  # 'success' is the name of the success page URL
    else:
        form = ContactForm()

    return render(request, "contact/contact_form.html", {"form": form})


def success_view(request):
    return render(request, "contact/success.html")
