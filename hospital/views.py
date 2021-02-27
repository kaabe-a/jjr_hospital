from django.shortcuts import render,get_object_or_404
from . forms import HospitalM_Form
from . models import HospitalM
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

def hospitalm_list_view(request):
	hospitals = HospitalM.objects.all()

	context	= {
		'hospitals':hospitals,
	}
	return render(request,'hospital/hospitalm_list_view.html',context)

@staff_member_required(login_url='login')
@login_required
def hospital_create_view(request):
	if request.method == 'POST':
		form = HospitalM_Form(request.POST)
		if form.is_valid():
			form.save()
			form = HospitalM_Form()
	else:
		form = HospitalM_Form()
	context = {
		'form':form,
	}
	return render(request,'hospital/hospital_create_view.html',context)

@user_passes_test(lambda u: u.is_superuser or u.is_staff,login_url='login')
def hospital_update_view(request,id):
	hospital = get_object_or_404(HospitalM,id=id)
	if request.method == 'POST':
		form = HospitalM_Form(request.POST,instance=hospital)
		if form.is_valid():
			form.save()
	else:
		form = HospitalM_Form(instance=hospital)
	context = {
		'form':form,
	}
	return render(request,'hospital/hospital_update_view.html',context)

@login_required
def hospital_detal_view(request,id):
	hospital = get_object_or_404(HospitalM,id=id)
	context = {
		'hospital':hospital,
	}
	return render(request,'hospital/hospital_detail_view.html',context)

@user_passes_test(lambda u: u.is_superuser, login_url='login')
def hospital_delete_view(request,id):
	hospital = get_object_or_404(HospitalM,id=id)
	if request.method == 'POST':
		hospital.delete()

	context = {
		'hospital':hospital,
	}
	return render(request,'hospital/hospital_delete_confirm_view.html',context)