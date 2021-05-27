from django.urls import path
from .views import home_view, myacc, mynone, register, chat

urlpatterns = [
	path('', home_view),
	path('myacc/', myacc),
	path('mynone/', mynone),
	path('register/', register),
	path('grats/', chat)
	]