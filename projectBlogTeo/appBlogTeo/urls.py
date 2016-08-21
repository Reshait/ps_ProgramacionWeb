from django.conf.urls import url

from . import views

app_name = 'appBlogTeo'
urlpatterns = [
	url(r'^$', views.ListadoHome, name='home'),
	url(r'^entrada/(?P<pk>.*)$', views.VistaEntradaCompleta.as_view(), name='VistaEntradaCompleta'),
    url(r'^acerca/$', views.VistaAcerca.as_view(), name='VistaAcerca'),

]
