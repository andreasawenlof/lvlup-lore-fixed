"""URLs for the contact app."""
from django.urls import path
from .views import contact_view, contact_messages_view, contact_message_detail_view, contact_toggle_read_view

urlpatterns = [
    path("", contact_view, name="contact"),
    path('contact-messages/', contact_messages_view, name='contact_messages'),
    path('contact-messages/<int:pk>/', contact_message_detail_view,
         name='contact_message_detail'),
    path('contact-messages/read/<int:pk>/',
         contact_toggle_read_view, name='contact_toggle_read'),
]
