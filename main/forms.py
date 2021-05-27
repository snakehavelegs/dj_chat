from django import forms
from .models import chat_user, chat_message

class LoginForm(forms.Form):
    username = forms.CharField(label='Username: ', max_length=100)
    password = forms.CharField(label='Password: ', widget= forms.PasswordInput, max_length=100)

class RegisterForm(LoginForm):
	name = forms.CharField(label='Name: ', max_length=100)
	email = forms.CharField(label='Email: ', widget=forms.EmailInput, max_length=100)

class ModelFormSave(RegisterForm, forms.ModelForm):
	class Meta:
		model = chat_user
		fields = "__all__"

class ChatForm(forms.Form):
	chatbox = forms.CharField(max_length=300, label=False)

class ChatModel(forms.ModelForm):
	class Meta:
		model = chat_message
		fields = ['message']


