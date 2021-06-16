from django.contrib import admin
from .models import chat_user, chat_message, in_room
# Register your models here.
admin.site.register(chat_user)
admin.site.register(chat_message)
admin.site.register(in_room)