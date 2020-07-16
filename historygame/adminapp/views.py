from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from authapp.models import GameUser

from adminapp.forms import AdminGameUserCreateForm, AdminGameUserUpdateForm
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from mainapp.models import CategoryGame, ProductGame
from mainapp.forms import GameCategoryForm, GameProductForm


class MethodSuperusers:
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserListView(ListView, MethodSuperusers):
    model = GameUser


class UserCreateView(CreateView, MethodSuperusers):
    model = GameUser
    success_url = reverse_lazy('my_admin:index')
    # fields = ['username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar', 'is_active']
    form_class = AdminGameUserCreateForm


class UserUpdateView(UpdateView, MethodSuperusers):
    model = GameUser
    success_url = reverse_lazy('my_admin:index')
    # fields = ['username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar', 'is_active']
    form_class = AdminGameUserUpdateForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'категории/редактирование'
    #
    #     return context


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     list_user = GameUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     content = {
#         'title': 'admin',
#         'list_user': list_user,
#     }
#     return render(request, 'adminapp/gameuser_list.html', content)


# @user_passes_test(lambda x: x.is_superuser)
# def create_user(request):
#     if request.method == 'POST':
#         form = AdminGameUserCreateForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('my_admin:index'))
#     else:
#         form = AdminGameUserCreateForm()
#     content = {
#         'title': 'create user',
#         'form': form,
#     }
#     return render(request, 'adminapp/create_user.html', content)
#

# @user_passes_test(lambda x: x.is_superuser)
# def update_user(request, pk):
#     user = get_object_or_404(GameUser , pk=pk)
#     if request.method == 'POST':
#         form = AdminGameUserUpdateForm(request.POST, request.FILES, instance=user)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('auth:update'))
#     else:
#         form = AdminGameUserUpdateForm(instance=user)
#     content = {
#         'title': 'update user',
#         'form': form,
#         'link': 'my_admin:index'
#     }
#     return render(request, 'adminapp/update.html', content)


@user_passes_test(lambda x: x.is_superuser)
def delete_user(request, pk):
    user = get_object_or_404(GameUser , pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:index'))

    content = {
        'title': 'update user',
        'delete_user': user,
    }
    return render(request, 'adminapp/delete_user.html', content)


@user_passes_test(lambda x: x.is_superuser)
def restore_user(request, pk):
    user = get_object_or_404(GameUser , pk=pk)
    if request.method == 'POST':
        user.is_active = True
        user.save()
        return JsonResponse(data={
            'pk': pk,
        })

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def category_product(request):
    list_category = CategoryGame.objects.all()
    content = {
        'title': 'categories',
        'list_category': list_category,
    }
    return render(request, 'adminapp/category_product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(CategoryGame, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return JsonResponse(data={
            'pk': pk,
        })

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def category_restore(request, pk):
    category = get_object_or_404(CategoryGame, pk=pk)
    if request.method == 'POST':
        category.is_active = True
        category.save()
        return JsonResponse(data={
            'pk': pk,
        })

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def category_update(request, pk):
    category = get_object_or_404(CategoryGame, pk=pk)
    if request.method == 'POST':
        form = GameCategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = form = GameCategoryForm(instance=category)
    content = {
        'title': 'update category',
        'form': form,
        'link': 'my_admin:category_product'
    }
    return render(request, 'adminapp/update.html', content)


@user_passes_test(lambda x: x.is_superuser)
def category_create(request):
    if request.method == 'POST':
        form = GameCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = GameCategoryForm()
    content = {
        'title': 'create category',
        'form': form,
        'link': 'my_admin:category_product'
    }

    return render(request, 'adminapp/update.html', content)


@user_passes_test(lambda x: x.is_superuser)
def products(request, pk):
    category = get_object_or_404(CategoryGame, pk=pk)
    list_products = ProductGame.objects.all().filter(category=category)
    content = {
        'title': category.name,
        'category': category.name,
        'list_category': list_products,
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(ProductGame, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return JsonResponse(data={
            'pk': pk,
        })

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def product_restore(request, pk):
    product = get_object_or_404(ProductGame, pk=pk)
    if request.method == 'POST':
        product.is_active = True
        product.save()
        return JsonResponse(data={
            'pk': pk,
        })

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(ProductGame, pk=pk)
    if request.method == 'POST':
        form = GameCategoryForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = form = GameCategoryForm(instance=product)
    content = {
        'title': 'update category',
        'form': form,
        'link': 'my_admin:category_product',
        # 'link': 'my_admin:products ' + product.category.pk,
    }
    return render(request, 'adminapp/update.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request):
    if request.method == 'POST':
        form = GameProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = GameProductForm()
    content = {
        'title': 'create product',
        'form': form,
        'link': 'my_admin:category_product'
    }
    return render(request, 'adminapp/update.html', content)
