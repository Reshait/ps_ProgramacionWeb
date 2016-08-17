from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .forms import RegistroUsuario
from .models import PerfilUsuario

# Create your views here.

def vistaRegistroUsuario(request):
#	if request.method == 'POST':
#		form = RegistroUsuario(request.POST, request.FILES)
#	else:
#		form = RegistroUsuario()
#	context = {'form':form}

#	return render(request, 'registro.html', context)

    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = RegistroUsuario(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            nombreUsuario = cleaned_data.get('nombreUsuario')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=nombreUsuario, password=password)
            # Anyadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = PerfilUsuario()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina cuentasUsuario/gracias.html
            # Pero lo hacemos con un redirect.
            return redirect(reverse('cuentasUsuario.gracias', kwargs={'nombreUsuario': nombreUsuario}))
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUsuario vacio
        form = RegistroUsuario()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'registro.html', context)


def vistaGracias(request, nombreUsuario):
    return render(request, 'gracias.html', {'nombreUsuario': nombreUsuario})
