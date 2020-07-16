
from django.contrib import admin
from django.urls import path, re_path

import mainapp.views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.views.index, name='main'),
    path('gallery/', mainapp.views.gallery, name='gallery'),
    # path('gallery/<int:page>/', mainapp.views.gallery, name='gallery'),

    path('gallery/<int:pk>/category/', mainapp.views.gallery, name='gallery'),
    path('gallery/<int:pk>/category/<int:page>/', mainapp.views.gallery, name='gallery'),

    path('contacts/', mainapp.views.contacts, name='contacts'),
    re_path(r'product/(?P<pk>\d+)/$', mainapp.views.product, name='product'),
]
