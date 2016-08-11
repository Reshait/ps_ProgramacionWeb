from django.conf.urls import url

from . import views

app_name = 'appBlogTeo'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^entrada/(?P<entrada_id>.*)$', views.entradaCompleta, name='entradaCompleta'),

]
