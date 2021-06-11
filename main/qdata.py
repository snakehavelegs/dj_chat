from .models import *
def go_message(username):
	data = chat_message.objects.raw('SELECT Name FROM chat_message WHERE username = %s', [username])
	