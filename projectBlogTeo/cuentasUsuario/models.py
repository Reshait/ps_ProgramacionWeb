from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.

class PerfilUsuario(models.Model):
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.usuario.username
