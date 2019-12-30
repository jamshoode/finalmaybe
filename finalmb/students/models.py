from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class basic_info(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()

class mapr(models.Model):
	marks = models.PositiveIntegerField()
	presence = models.BooleanField()
	bi = models.ForeignKey(basic_info,
	on_delete=models.PROTECT)
