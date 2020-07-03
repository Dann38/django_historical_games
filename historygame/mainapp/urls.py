
from django.contrib import admin
from django.urls import path, re_path

import mainapp.views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.views.index, name='main'),
    path('gallery/', mainapp.views.gallery, name='gallery'),

    re_path(r'gallery/(?P<pk>\d+)/category', mainapp.views.gallery_category, name='gallery_category'),
    path('gallery/<int:pk>/category', mainapp.views.gallery_category, name='gallery_category'),

    path('contacts/', mainapp.views.contacts, name='contacts'),
    re_path(r'product/(?P<pk>\d+)/', mainapp.views.product, name='product'),
]
