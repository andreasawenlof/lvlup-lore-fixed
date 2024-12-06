from .views import modal_login_view
from django.urls import path
urlpatterns = [
    path("login/", modal_login_view, name="modal_login")
]
