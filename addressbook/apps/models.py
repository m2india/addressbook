from django.db import models

class add(models.Model):

	name = models.CharField(max_length=300)
	dateofbirth = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	state = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
