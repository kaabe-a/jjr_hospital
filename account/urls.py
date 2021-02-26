from django.urls import path,include
from . views import register,profile,dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('register/',register,name='register'),
		path('dashboard/',dashboard,name='dashboard'),
		path('profile/<username>/',profile,name='profile'),
    	path('',include('django.contrib.auth.urls')),
	]