from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
#from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Para formularios:
from django.forms import ModelForm
#from django.core.context_processors import csrf #--> para versiones > django 1.10
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
    success_url = reverse_lazy('home')

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
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VistaContacto, self).get_context_data(**kwargs)
        context['listadoTitulos'] = ListadoTitulos()
        return context


