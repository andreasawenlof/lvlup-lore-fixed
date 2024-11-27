from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages


def ajax_login_form(request):

""" Render login form for AJAX model """
form.loginForm()
return render(request, 'auth/login_form.html', {'form': form})
