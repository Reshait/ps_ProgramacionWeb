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
		return Entrada.objects.order_by('-fecha')[:4]

class VistaEntradaCompleta(generic.DetailView):
	model = Entrada
	template_name = 'entradaCompleta.html'
