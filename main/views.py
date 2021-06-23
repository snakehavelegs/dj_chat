from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import chat_user,chat_message, in_room
from .forms import LoginForm, RegisterForm, ModelFormSave, ChatForm, ModelChatFormSave
from .serializers import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser, FormParser


def home_view(request):
	if request.method == "POST":
		in_room.objects.all().delete()
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
			name = checkuser.name
			in_room(users=name).save()
			return HttpResponseRedirect('chat/')
	
		else:
			form = LoginForm()
			return render(request, 'incorrect/incorrect.html', {'form': form})
	
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form': form})

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
	message= ""
	getmsg = chat_message.objects.all()
	if request.method == "POST":
		chatform = ModelChatFormSave(request.POST)
		if chatform.is_valid():
			cdata= chatform.cleaned_data['message']
			msg=chat_message.objects.create(message=cdata, sender = in_room.objects.all()[0], chatuser=chat_user.objects.get(name=in_room.objects.all()[0]))
			chatform = ModelChatFormSave()
	return render(request, 'grats/grats.html', {'chatform': chatform, 'message': message, 'getmsg': getmsg})

