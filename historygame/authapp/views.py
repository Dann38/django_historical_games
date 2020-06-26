from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import GameUserLoginForm
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