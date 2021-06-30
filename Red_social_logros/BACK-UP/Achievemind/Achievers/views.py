from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm



def welcome(request):
	return render(request, "Achievers/welcome.html")
	
def enter(request):				
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				do_login(request, user)
				return redirect('/')
	return render(request, "Achievers/enter.html", {'form': form})
	
def register(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				do_login(request, user)
				return redirect('/')
	return render(request, "Achievers/register.html", {'form': form})
	
def forgotPassword(request):
	return render(request, "Achievers/forgotPassword.html")
	
def profile(request):
	return render(request, "Achievers/profile.html")
	
def logout(request):
	do_logout(request)
	return redirect('/')
