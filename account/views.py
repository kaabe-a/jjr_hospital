from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login as auth_login,authenticate, logout as auth_logout
from . forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from hospital.models import HospitalM

@login_required(login_url='login')
def dashboard(request):
	if request.user.is_superuser:
		hospitals = HospitalM.objects.all()
		users = User.objects.all()
		return render(request,'account/dashboard.html',{'hospitals':hospitals,'users':users,})
	elif request.user.is_staff:
		hospitals = HospitalM.objects.all()
	else:
		hospitals = HospitalM.objects.all()
	context	=	{
		'hospitals':hospitals,
	}
	return render(request,'account/dashboard.html',context)


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.set_password(
				form.cleaned_data['password']
				)
			new_form.save()
			return render(request,'account/dashboard.html',{'new_user':new_form})
	else:
		form=UserRegistrationForm()
	return render(request,'registration/register.html',{'form':form})

@login_required
def profile(request,username):
	username = get_object_or_404(User,username=username)
	print(username)
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,data = request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

		if user_form.is_valid and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,'Profile have been updated successfuly')
		else:
			messages.error(request,'Sorry some thing went wrong Please try again')

	else:
		user_form=UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request,'account/profile.html',{'user_form':user_form,'profile_form':profile_form})

