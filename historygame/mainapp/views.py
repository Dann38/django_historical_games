from django.shortcuts import render
from mainapp.models import CategoryGame, ProductGame
from django.shortcuts import get_object_or_404


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


def gallery_category(request, pk):
    categories = CategoryGame.objects.all()
    # if pk == '0':
    #     products = ProductGame.objects.all()
    #     category = {'name': 'all', 'pk': '0'}
    # else:
    category = get_object_or_404(CategoryGame, pk=pk)
    products = ProductGame.objects.filter(category__pk=pk).order_by('price')
    content = {
        'title': 'gallery',
        'categories': categories,
        'products': products,
        'category': category,
    }
    return render(request, 'mainapp/gallery_category.html', content)
