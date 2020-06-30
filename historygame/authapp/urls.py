from django.urls import path

import authapp.views

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.views.login, name='login'),
    path('logout/', authapp.views.logout, name='logout'),
    path('register/', authapp.views.register, name='register'),
    path('update/', authapp.views.update, name='update'),
]
