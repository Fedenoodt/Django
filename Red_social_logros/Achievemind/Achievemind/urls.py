from django.contrib import admin
from django.urls import path
from Achievers import views


urlpatterns = [
	path('', views.welcome),
	path('enter', views.enter),
	path('register', views.register),
	path('profile', views.profile),
	path('logout', views.logout),
	
	path('admin/', admin.site.urls),
]
