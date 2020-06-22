from django.shortcuts import render


def index(request):
    content = {
        'title': 'main',
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    content = {
        'title': 'contacts',
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request):
    content = {
        'title': 'gallery',
    }
    return render(request, 'mainapp/gallery.html', content)


def product(request):
    content = {
        'title': 'product',
    }
    return render(request, 'mainapp/page_product.html', content)