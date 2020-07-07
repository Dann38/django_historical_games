from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from authapp.models import GameUser

from adminapp.forms import AdminGameUserCreateForm, AdminGameUserUpdateForm
from django.urls import reverse


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    list_user = GameUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'title': 'admin',
        'list_user': list_user,
    }
    return render(request, 'adminapp/index.html', content)


@user_passes_test(lambda x: x.is_superuser)
def create_user(request):
    if request.method == 'POST':
        form = AdminGameUserCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        form = AdminGameUserCreateForm()
    content = {
        'title': 'create user',
        'form': form,
    }
    return render(request, 'adminapp/create_user.html', content)


@user_passes_test(lambda x: x.is_superuser)
def update_user(request, pk):
    user = get_object_or_404(GameUser, pk=pk)
    if request.method == 'POST':
        form = AdminGameUserUpdateForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = AdminGameUserUpdateForm(instance=user)
    content = {
        'title': 'update user',
        'form': form,
    }
    return render(request, 'adminapp/update_user.html', content)


def delete_user(request, pk):
    user = get_object_or_404(GameUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:index'))

    content = {
        'title': 'update user',
        'delete_user': user,
    }
    return render(request, 'adminapp/delete_user.html', content)


def restore_user(request, pk):
    user = get_object_or_404(GameUser, pk=pk)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('my_admin:index'))

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))