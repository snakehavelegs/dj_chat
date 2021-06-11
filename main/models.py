from django.db import models


# Create your models here.

class chat_user(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=50, default='SOMESTRING')
	password = models.CharField(max_length=50, default='SOMESTRING')

	def __str__(self):
		return self.name

class chat_message(models.Model):
	chatuser = models.ForeignKey(chat_user, on_delete = models.CASCADE, null=True, default=None)
	sender = models.CharField(max_length=300, null= True, default=None)
	message = models.CharField(max_length=300)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message

