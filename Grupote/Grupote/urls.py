"""Grupote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import login
from usuario.views import entradaGrupote, ingreso, nexo, nuevoArticulo
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^entradaGrupote/', include('apps.entradaGrupote.urls', namespace = 'entradaGrupote')),
    url(r'^nexo/', include('apps.nexo.urls', namespace = 'nexo')),
    url(r'^nuevoArticulo/', include('apps.nuevoArticulo.urls', namespace = 'nuevoArticulo')),
    url(r'^$', login, {'template_name' : 'ingresoGrupote.html'}, name = 'login')
]
