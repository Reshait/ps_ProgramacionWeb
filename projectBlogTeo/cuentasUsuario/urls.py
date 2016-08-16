from django.conf.urls import url, include
from django.contrib import admin
from cuentasUsuario import views

urlpatterns = [
	url(r'^registro/$', views.vistaRegistroUsuario, name='cuentasUsuario.vistaRegistroUsuario')
]
