from django.core.paginator import Paginator, EmptyPage
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


def gallery(request, pk=0, page=1):
    categories = CategoryGame.objects.all()
    if pk == 0:
        category = {
            'pk': 0,
            'name': 'all',
        }
        products = ProductGame.objects.all()
    else:
        category = get_object_or_404(CategoryGame, pk=pk)
        products = ProductGame.objects.filter(category__pk=pk).order_by('price')

    product_paginator = Paginator(products, 8)
    try:
        prd = product_paginator.page(page)
    except EmptyPage:
        prd = product_paginator.page(product_paginator.num_pages)

    content = {
        'title': 'gallery',
        'categories': categories,
        'products': prd,
        'category': category,
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
