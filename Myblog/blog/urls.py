from django.conf.urls import url, patterns, include
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^client/$', views.client, name='clients'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.show_article, name='article'),
]