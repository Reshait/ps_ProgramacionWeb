from django.shortcuts import render

from .forms import RegistroUsuario

# Create your views here.

def vistaRegistroUsuario(request):
	if request.method == 'POST':
		form = RegistroUsuario(request.POST, request.FILES)
	else:
		form = RegistroUsuario()
	context = {'form':form}

	return render(request, 'registro.html', context)