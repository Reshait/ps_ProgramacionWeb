from django.conf.urls import url, include
from django.contrib import admin
from cuentasUsuario import views

urlpatterns = [
    url(r'^$', views.vistaIndex, name='cuentasUsuario.index'),
    url(r'^login/$', views.vistaLogin, name='cuentasUsuario.login'),
    url(r'^logout/$', views.vistaLogout, name='cuentasUsuario.logout'),

	url(r'^registro/$', views.vistaRegistroUsuario, name='cuentasUsuario.vistaRegistroUsuario'),
	url(r'^gracias/(?P<nombreUsuario>[\w]+)/$', views.vistaGracias, name='cuentasUsuario.vistaGracias'),
	url(r'^editarEmail/$', views.editar_email, name='cuentasUsuario.editar_email'),

]
