from django.urls import path

import adminapp.views

app_name = 'adminapp'

urlpatterns = [
    # path('main/', adminapp.views.index, name='index'),
    # path('create_user/', adminapp.views.create_user, name='create_user'),
    # path('update_user/<int:pk>/', adminapp.views.update_user, name='update_user'),
    path('main/', adminapp.views.UserListView.as_view(), name='index'),
    path('create_user/', adminapp.views.UserCreateView.as_view(), name='create_user'),
    path('update_user/<int:pk>/', adminapp.views.UserUpdateView.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', adminapp.views.delete_user, name='delete_user'),
    path('restore_user/<int:pk>/', adminapp.views.restore_user, name='restore_user'),

    path('category_product/', adminapp.views.category_product, name='category_product'),
    path('category_product/category_delete/<int:pk>/', adminapp.views.category_delete, name='category_delete'),
    path('category_product/category_restore/<int:pk>/', adminapp.views.category_restore, name='category_restore'),
    path('category_product/category_update/<int:pk>/', adminapp.views.category_update, name='category_update'),
    path('category_product/category_create/', adminapp.views.category_create, name='category_create'),

    path('category_product/<int:pk>/products/', adminapp.views.products, name='products'),
    path('category_product/products/delete/<int:pk>/', adminapp.views.product_delete, name='product_delete'),
    path('category_product/products/restore/<int:pk>/', adminapp.views.product_restore, name='product_restore'),
    path('category_product/products/update/<int:pk>/', adminapp.views.product_update, name='product_update'),
    path('category_product/products/product_create/', adminapp.views.product_create, name='product_create'),

]
