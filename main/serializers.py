from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = chat_message
		fields = '__all__'