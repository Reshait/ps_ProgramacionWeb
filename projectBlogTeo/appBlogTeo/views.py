from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Entrada

# Create your views here.

class VistaHome(generic.ListView):
	template_name = 'home.html'
	context_object_name = 'listadoEntradas'

	def get_queryset(self):
		listado = Entrada.objects.order_by('-fecha')[:4]
		for i in listado:
			if len(i.cuerpo) >= 150:
				i.cuerpo = i.cuerpo[0:150] + "...      -> leer +"

		return listado

class VistaEntradaCompleta(generic.DetailView):
	model = Entrada
	template_name = 'entradaCompleta.html'
