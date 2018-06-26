from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^signin$', views.signin),
	url(r'^signin_form$', views.signin_form),
	url(r'^register$', views.register),
	url(r'^register_form$', views.register_form)
]