from django.urls import path

import adminapp.views

app_name = 'adminapp'

urlpatterns = [
    path('main/', adminapp.views.index, name='index'),
    path('create_user/', adminapp.views.create_user, name='create_user'),
    path('update_user/<int:pk>/', adminapp.views.update_user, name='update_user'),
    path('delete_user/<int:pk>/', adminapp.views.delete_user, name='delete_user'),
    path('restore_user/<int:pk>/', adminapp.views.restore_user, name='restore_user'),

]
