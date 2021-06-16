from django.urls import path
from .views import home_view, register, chat

urlpatterns = [
	path('', home_view),
	path('register/', register),
	path('chat/', chat)
	]