from django.urls import path

from .consumers import Chat

ws_urlpatterns = [
    path("ws/chat/", Chat.as_asgi())
]
