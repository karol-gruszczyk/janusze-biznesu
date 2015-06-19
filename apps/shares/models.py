from django.db import models

# Create your models here.

class Share(models.Model):

	name = models.CharField(max_length=32)
	updated_daily = models.BooleanField()