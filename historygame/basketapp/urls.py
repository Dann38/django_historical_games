
from django.contrib import admin
from django.urls import path, re_path

import basketapp.views

app_name = 'basketapp'

urlpatterns = [
    re_path(r'basket_add/(?P<pk>\d+)/', basketapp.views.basket_add, name='basket_add'),
    re_path(r'basket_delete/(?P<pk>\d+)/', basketapp.views.basket_delete, name='basket_delete'),
    re_path(r'basket/', basketapp.views.index, name='index')
]
