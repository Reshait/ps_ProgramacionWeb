from django.shortcuts import render
from .models import Entrada

# Create your views here.
def home(request):
	listadoEntradas = Entrada.objects.order_by('-fecha')[:4]
	context = {'listadoEntradas': listadoEntradas}
	return render(request, 'home.html', context)

#def entradaCompleta(request):

