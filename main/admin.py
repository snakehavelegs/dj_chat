from django.contrib import admin
from .models import chat_user, chat_message
# Register your models here.
admin.site.register(chat_user)
admin.site.register(chat_message)