from django.db import models

class HospitalM(models.Model):
	Unitname = models.CharField(max_length=56)
	Allbeds = models.IntegerField(blank=False, null=False)
	Occupiedbeds = models.IntegerField(blank=False, null=False)
	Impedingbeds  = models.IntegerField(blank=False, null=False)

	@property
	def freebeds(self):
		return self.Allbeds-self.Occupiedbeds-self.Impedingbeds

	def __str__(self):
		return self.Unitname


	

