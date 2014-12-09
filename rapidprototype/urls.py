from django.conf.urls import patterns, include, url
from .views import page
from django.contrib import admin

urlpatterns = (
	url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
	url(r'^$', page, name='homepage')
	)
