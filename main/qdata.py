from .models import *
def go_message(username):
	data = chat_message.objects.raw('SELECT * FROM chat_message WHERE username = %s', [username])
	data.save()