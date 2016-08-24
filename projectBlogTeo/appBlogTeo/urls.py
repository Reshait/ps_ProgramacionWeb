from django.conf.urls import url

from . import views

app_name = 'appBlogTeo'
urlpatterns = [
	url(r'^$', views.ListadoHome.as_view(), name='home'),
	url(r'^entrada/(?P<pk>.*)$', views.VistaEntradaCompleta.as_view(), name='VistaEntradaCompleta'),
    url(r'^acerca/$', views.VistaAcerca.as_view(), name='acerca'),
    url(r'^contact/$', views.VistaContacto.as_view(), name='contacto'),
    url(r'^crear/$', views.EntradaCrearVista.as_view(), name='crear'),
]
