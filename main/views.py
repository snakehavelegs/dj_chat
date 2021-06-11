from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import chat_user,chat_message
from .forms import LoginForm, RegisterForm, ModelFormSave, ChatForm, ModelChatFormSave
from .serializers import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser, FormParser
global CURR_USER
global checkuser
CURR_USER = list()

def home_view(request):
	if request.method == "POST":
		form = LoginForm()
		username = request.POST['username']
		password = request.POST['password']
		try:
			global checkuser
			checkuser = chat_user.objects.get(username=username, password=password)
			
		except:
			form = LoginForm()
			return render(request, 'incorrect/incorrect.html', {'form': form})
		
		if checkuser is not None:
			global CURR_USER
			CURR_USER.append('Artur')
			return HttpResponseRedirect('chat/')
	
		else:
			form = LoginForm()
			return render(request, 'incorrect/incorrect.html', {'form': form})
	
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form': form})

def myacc(request):
	return HttpResponse('<h1>Nice!</h1>')

def mynone(request):
	return HttpResponse('<h1>Fuk!</h1>')

def register(request):
	if request.method == "POST":
		register = ModelFormSave(request.POST)
		if register.is_valid():
			register.save()
			HttpResponseRedirect('/')

	else:
		register = ModelFormSave()
	return render(request, 'registration/register.html', {'register': register})

def chat(request):
	chatform = ModelChatFormSave()
	if request.method == "POST":
		chatform = ModelChatFormSave(request.POST)
		if chatform.is_valid():
			global CURR_USER
			cdata= chatform.cleaned_data['message']
			chat_message.objects.create(message=cdata, sender=CURR_USER, chatuser=chat_user.objects.get(name="Artur"))
	return render(request, 'grats/grats.html', {'chatform': chatform})