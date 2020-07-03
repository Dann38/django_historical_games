from django.shortcuts import render
from mainapp.models import CategoryGame, ProductGame
from django.shortcuts import get_object_or_404


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket_set.all()
    else:
        return []


def index(request):
    products = ProductGame.objects.all()
    content = {
        'title': 'main',
        'products': products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    content = {
        'title': 'contacts',
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contacts.html', content)


def gallery(request):
    categories = CategoryGame.objects.all()
    products = ProductGame.objects.all()
    content = {
        'title': 'gallery',
        'categories': categories,
        'products': products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/gallery.html', content)


def product(request, pk):
    product = get_object_or_404(ProductGame, pk=pk)
    products = ProductGame.objects.filter(category=product.category)
    content = {
        'product': product,
        'title': 'product',
        'products': products,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/page_product.html', content)


def gallery_category(request, pk):
    categories = CategoryGame.objects.all()

    category = get_object_or_404(CategoryGame, pk=pk)
    products = ProductGame.objects.filter(category__pk=pk).order_by('price')
    content = {
        'title': 'gallery',
        'categories': categories,
        'products': products,
        'category': category,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/gallery_category.html', content)
