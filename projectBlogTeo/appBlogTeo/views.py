from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Para formularios:
from django.forms import ModelForm
#from django.core.context_processors import csrf #--> para versiones > django 1.10
from django.views.decorators import csrf


from .models import Entrada

# Create your views here.

## Antes de Paginator

#class VistaHome(generic.ListView):
#	template_name = 'home.html'
#	context_object_name = 'listadoEntradas'
#
#	def get_queryset(self):
#		listado = Entrada.objects.order_by('-fecha')[:4]
#		for i in listado:
#			if len(i.cuerpo) >= 150:
#				i.cuerpo = i.cuerpo[0:150] + "...      -> leer +"
#
#		return listado

def ListadoHome(request):
    listadoEntradas = Entrada.objects.all()
    paginator = Paginator(listadoEntradas, 4) # Show 25 contacts per page

    for i in listadoEntradas:
		if len(i.cuerpo) >= 150:
			i.cuerpo = i.cuerpo[0:150] + "...      -> leer +"

    listadoEntradasPagina = request.GET.get('listadoEntradasPagina')

    try:
        entradas = paginator.page(listadoEntradasPagina)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        entradas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        entradas = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'listadoEntradas': entradas})


class VistaEntradaCompleta(generic.DetailView):
	model = Entrada
	template_name = 'entradaCompleta.html'


class VistaAcerca(generic.View):

    def get(self, request, *args, **kwarg):
        return render(request, 'acerca.html')
