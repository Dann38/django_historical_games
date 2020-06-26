from django.shortcuts import render
from mainapp.models import CategoryGame, ProductGame


def index(request):
    products = ProductGame.objects.all()
    content = {
        'title': 'main',
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    content = {
        'title': 'contacts',
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request):
    categories = CategoryGame.objects.all()
    products = ProductGame.objects.all()
    content = {
        'title': 'gallery',
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/gallery.html', content)


def product(request):
    products = ProductGame.objects.all()
    content = {
        'title': 'product',
        'products': products,
    }
    return render(request, 'mainapp/page_product.html', content)