from django.shortcuts import render

# Create your views here.

def entradaGrupote(request):
	return render(request, "usuario/nexoGrupote.html")