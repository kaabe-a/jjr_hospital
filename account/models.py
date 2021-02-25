from django.db import models
from django.db.models.signals import post_save,pre_save
from django.conf import settings
from django.urls import reverse
User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
user_model= get_user_model()

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True,null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

	def __str__(self):
		return self.user.username
	# def get_absolute_url(self):
		


def profile_post_receiver_save(instance,sender,created,*args,**kwargs):
	if created:
		try:
			Profile.objects.create(user = instance)
		except:
			pass

post_save.connect(profile_post_receiver_save,sender=User)
