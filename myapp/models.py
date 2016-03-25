from django.db import models
from django.utils import timezone

# Create your models here.
class URL(models.Model):
	myurl = models.URLField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.myurl
	

