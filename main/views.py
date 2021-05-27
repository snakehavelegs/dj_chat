from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import chat_user,chat_message
from .forms import LoginForm, RegisterForm, ModelFormSave, ChatForm, ChatModel
from .qdata import *


def home_view(request):
	if request.method == "POST":
		form = LoginForm()
		username = request.POST['username']
		password = request.POST['password']
		try:
			checkuser = chat_user.objects.get(username=username, password=password)
		except:
			form = LoginForm()
			return render(request, 'incorrect/incorrect.html', {'form': form})
		
		if checkuser is not None:
			go_message(checkuser)
			return HttpResponseRedirect('/grats')
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
	chatform = ChatForm()
	if request.method == "POST":
		message = ChatModel(request.POST)
		if message.is_valid():
			message.save()
	return render(request, 'grats/grats.html', {'chatform': chatform})
