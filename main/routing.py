from django.urls import path

from . import consumers
from .consumers import WSConsumer

ws_urlpatterns = [
    path('chat/', WSConsumer.as_asgi())
]