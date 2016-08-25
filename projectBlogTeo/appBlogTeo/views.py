from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Para formularios:
from django.forms import ModelForm
#from django.core.context_processors import csrf #--> para versiones < django 1.10
from django.views.decorators import csrf

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from .forms import ContactoForm
from .models import Entrada


# Create your views here.

def ListadoTitulos():
    listadoTitulos = Entrada.objects.all()[:10]
    return listadoTitulos

#Hecho sin vista:
#def ListadoHome(request):
#    listadoEntradas = Entrada.objects.all()
#    paginator = Paginator(listadoEntradas, 4) 
#
#    for i in listadoEntradas:
#		if len(i.cuerpo) >= 150:
#			i.cuerpo = i.cuerpo[0:150] 
#
#    listadoEntradasPagina = request.GET.get('listadoEntradasPagina')
#
#    try:
#        entradas = paginator.page(listadoEntradasPagina)
#    except PageNotAnInteger:
#        # If page is not an integer, deliver first page.
#        entradas = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range (e.g. 9999), deliver last page of results.
#        entradas = paginator.page(paginator.num_pages)
#
#    return render(request, 'home.html', {'listadoEntradas': entradas, 'listadoTitulos':ListadoTitulos()})

# Para hacerlo con clases, en las url hay que aniadir .as_view() a la vista
class ListadoHome(generic.ListView):
    context_object_name = 'listadoEntradas'
    model = Entrada
    template_name = 'home.html'
    paginate_by = 4

    #En este formato, las palabras se acortan en el html con entrada.cuerpo|slice:":140"
    def get_context_data(self, **kwargs):
        context = super(ListadoHome, self).get_context_data(**kwargs)
        context['listadoTitulos'] = ListadoTitulos()
        return context


class VistaEntradaCompleta(generic.DetailView):
    model = Entrada
    template_name = 'entradaCompleta.html'

    def get_context_data(self, **kwargs):
        context = super(VistaEntradaCompleta, self).get_context_data(**kwargs)
        context['listadoTitulos'] = ListadoTitulos()
        return context


class VistaAcerca(generic.View):

    def get(self, request, *args, **kwarg):
        return render(request, 'acerca.html', {'listadoTitulos':ListadoTitulos()})


def send_email_contact(email_usuario, subject, body):
    body = '{} ha enviado un email de contacto\n\n{}\n\n{}'.format(email_usuario, subject, body)
    send_mail(
        subject='Nuevo email de contacto',
        message=body,
        from_email='contact@example.com',
        recipient_list=['usuario@example.com']
    )

class VistaContacto(generic.FormView):

    template_name = 'contacto.html'
    success_url = reverse_lazy('home:home')

    def dispatch(self, request, *args, **kwargs):
        self.form_class = ContactoForm
        return super(VistaContacto, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        subject = form.cleaned_data.get('subject')
        body = form.cleaned_data.get('body')
        if self.request.user.is_authenticated():
            email_usuario = self.request.user.email
            send_email_contact(email_usuario, subject, body)
        else:
            email_usuario = form.cleaned_data.get('email')
            send_email_contact(email_usuario, subject, body)
        messages.success(self.request, 'Email enviado con exito')
        return super(VistaContacto, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VistaContacto, self).get_context_data(**kwargs)
        context['listadoTitulos'] = ListadoTitulos()
        return context

class EntradaCrearVista(generic.CreateView):
    template_name = 'entradaForm.html'
    model = Entrada
    fields = ('titulo', 'cuerpo')
    success_url = reverse_lazy('home:crear')

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super(EntradaCrearVista, self).get_context_data(**kwargs)
        # anyadimos nuevas variables de contexto al diccionario
        context['titulo'] = 'Crear articulo'
        context['nombre_btn'] = 'Crear'
        context['listadoTitulos'] = ListadoTitulos()

        # devolvemos el contexto
        return context

    def dispatch(self, request, *args, **kwargs):
    # Comprueba si es usuario y
    # tiene permisos para anyadir un articulo, si no lo tiene, lo
    # redirecciona a login
    #       Redireccionar a pagina de login
        if not request.user.has_perms('blog.add_entrada'):
            return redirect(settings.LOGIN_URL)
        return super(EntradaCrearVista, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Entrada enviada correctamente')
        return super(EntradaCrearVista, self).form_valid(form)   


class EntradaActualizarVista(generic.UpdateView):
    template_name = 'entradaForm.html'
    model = Entrada
    fields = ('titulo', 'cuerpo')
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super(EntradaActualizarVista, self).get_context_data(**kwargs)
        # anyadimos nuevas variables de contexto al diccionario
        context['title'] = 'Editar articulo'
        context['nombre_btn'] = 'Editar'
        context['listadoTitulos'] = ListadoTitulos()
        # devolvemos el contexto
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.change_entrada'):
            return redirect(settigns.LOGIN_URL)
        return super(EntradaActualizarVista, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Entrada editada correctamente')
        return super(EntradaActualizarVista, self).form_valid(form)


class EntradaBorrarVista(generic.DeleteView):

    template_name = 'confirmarEliminacion.html'
    success_url = reverse_lazy('home:home')
    model = Entrada

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.delete_entrada'):
            return redirect(settings.LOGIN_URL)
        return super(EntradaBorrarVista, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EntradaBorrarVista, self).get_context_data(**kwargs)
        context['listadoTitulos'] = ListadoTitulos()
        # devolvemos el contexto
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Entrada eliminada correctamente')
        return super(EntradaBorrarVista, self).form_valid(form)


