from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import GameUserLoginForm, GameUserRegisterForm, GameUserUpdateForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = GameUserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:main'))
    else:
        form = GameUserLoginForm()
    content = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))


def register(request):
    if request.method == 'POST':
        form = GameUserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:main'))
    else:
        form = GameUserRegisterForm()
    content = {
        'title': 'registration',
        'form': form,
    }
    return render(request, 'authapp/register.html', content)



def update(request):
    if request.method == 'POST':
        form = GameUserUpdateForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = GameUserUpdateForm(instance=request.user)
    content = {
        'title': 'update',
        'form': form,
    }
    return render(request, 'authapp/update.html', content)

