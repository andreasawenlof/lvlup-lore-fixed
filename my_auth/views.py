from django.http import JsonResponse
from django.shortcuts import render
from allauth.account.forms import LoginForm
from django.template.loader import render_to_string


def modal_login_view(request):
    form = LoginForm()
    if request.method == "GET":
        html = render_to_string(
            "my_auth/modal_login.html", {"form": form}, request=request)
        return JsonResponse({"html": html})
    return JsonResponse({"error": "Invalid request method"}, status=400)
