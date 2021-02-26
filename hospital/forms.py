from django import forms
from . models import HospitalM

class HospitalM_Form(forms.ModelForm):
	class Meta:
		model = HospitalM
		fields = '__all__'