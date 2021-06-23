"""
ASGI config for dj_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from main.routing import ws_urlpatterns

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_chat.settings')

application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
	#JUST HTTP FOR NOW
	})
