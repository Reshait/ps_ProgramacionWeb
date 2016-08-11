from django.conf.urls import url

from . import views

app_name = 'appBlogTeo'
urlpatterns = [
	url(r'^$', views.VistaHome.as_view(), name='home'),
	url(r'^entrada/(?P<pk>.*)$', views.VistaEntradaCompleta.as_view(), name='VistaEntradaCompleta'),
]
