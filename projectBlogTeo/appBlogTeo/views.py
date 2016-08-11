from django.shortcuts import render, get_object_or_404
from .models import Entrada

# Create your views here.
def home(request):
	listadoEntradas = Entrada.objects.order_by('-fecha')[:4]
	context = {'listadoEntradas': listadoEntradas}
	return render(request, 'home.html', context)

def entradaCompleta(request, entrada_id):
	entrada = get_object_or_404(Entrada, pk=entrada_id)
	return render(request, 'entradaCompleta.html', {'entrada':entrada})

