from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import * 

def index(request):
	return render(request, "wall/index.html")

def signin(request):
	return render(request, "wall/signin.html")

def register(request):
	return render(request, "wall/register.html")

def signin_form(request):
	result = User.objects.login_validator(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/signin')
	else:
		if result.user_level == 1:
			request.session['user_id'] = result.id
			return redirect('/dashboard')
		else:
			request.session['user_id'] = result.id
			return redirect('/dashboard/admin')

def register_form(request):
	result = User.objects.register_validator(request.POST)
	if type(result) == list:
		for error in result:
			messages.error(request, error)
		return redirect('/register')
	else:
		if result.user_level == 1:
			request.session['user_id'] = result.id
			return redirect('/dashboard')
		else:
			request.session['user_id'] = result.id
			return redirect('/dashboard/admin')