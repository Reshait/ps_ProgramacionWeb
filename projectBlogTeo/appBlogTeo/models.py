from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Entrada(models.Model):
	titulo = models.CharField(max_length = 100)
	cuerpo = models.TextField()
	fecha = models.DateTimeField(default=datetime.now, blank=True)
	#actualizacion = models.DateTimeField(auto_now=True)
	#propietario = models.ForeignKey(User)
	etiquetas = models.ManyToManyField('Etiqueta', blank=True)

	def __unicode__ (self):
		return self.titulo

	class Meta:
		ordering = ['-fecha']
    

class Etiqueta(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	slug = models.CharField(max_length=100, unique=True)

class Comentario(models.Model):
	fechaComentario = models.DateTimeField(auto_now_add=True)
	autor = models.CharField(max_length = 100, default= 'Anonimo')
	cuerpoComentario = models.TextField()
	idEntrada = models.ForeignKey(Entrada)

	def __unicode__ (self):
			return unicode("%s %s " % (self.idEntrada, self.cuerpoComentario[:60]))

