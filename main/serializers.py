from rest_framework import serializers
from .models import chat_user, chat_message
from .views import *

class MessageSerializer(serializers.ModelSerializer):
	chatuser = serializers.SlugRelatedField(many=False, slug_field='name', queryset=chat_user.objects.all())
	class Meta:
		model = chat_message
		fields = ['chatuser', 'message']