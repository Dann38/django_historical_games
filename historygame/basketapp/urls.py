
from django.contrib import admin
from django.urls import path, re_path

import basketapp.views

app_name = 'basketapp'

urlpatterns = [
    re_path(r'basket_add/(?P<pk>\d+)', basketapp.views.basket_add, name='basket_add'),
]
