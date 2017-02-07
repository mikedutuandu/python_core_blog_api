from django.conf.urls import url
from django.contrib import admin

from .views import post_list,post_detail,post_category_list


urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^the-loai/(?P<slug>[\w-]+)/$', post_category_list, name='category_list'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]
