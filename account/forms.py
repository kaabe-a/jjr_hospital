from django import forms
from django.contrib.auth.models import User
from . models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='password',widget=forms.PasswordInput())
	password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput())
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username','email','first_name','is_staff','is_superuser')


	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('passwords Dont match please')
		return cd['password2']
	def clean_email(self,*args,**kwargs):
		instance = self.instance
		print(instance)


class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth','photo')
		widgets = {
			'date_of_birth': forms.DateInput(attrs={'type':'date'})
		}