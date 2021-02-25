from django.urls import path,include
from . views import register,profile
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('register/',register,name='register'),
		path('profile/<username>/',profile,name='profile'),
    	path('',include('django.contrib.auth.urls')),
	]