from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Entrada(models.Model):
	titulo = models.CharField(max_length = 100)
	cuerpo = models.TextField()
	fecha = models.DateTimeField(default=datetime.now, blank=True)

	def __unicode__ (self):
		return self.titulo

	class Meta:
		ordering = ["-fecha"]
