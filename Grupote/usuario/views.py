from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def entradaGrupote(request):
	return render(request, "usuario/entradaGrupote.html", {})

def ingreso(request):				
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
	return render(request, "usuario/ingresoGrupote.html", {'form': form})

def nexo(request):
	return render(request, "usuario/nexoGrupote.html", {})