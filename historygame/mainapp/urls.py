
from django.contrib import admin
from django.urls import path

import mainapp.views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.views.index, name='main'),
    path('gallery/', mainapp.views.gallery, name='gallery'),
    path('contacts/', mainapp.views.contacts, name='contacts'),
    path('products/', mainapp.views.product, name='product'),
]
