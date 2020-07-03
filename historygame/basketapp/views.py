from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductGame
from basketapp.models import Basket


@login_required
def basket_add(request, pk):
    product = get_object_or_404(ProductGame, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    # basket = request.user.basket_set(product=pk).first
    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def index(request):
    basket = Basket.objects.filter(user=request.user)
    context = {
       'basket': basket,
    }
    return render(request, 'basketapp/index.html', context=context)


@login_required
def basket_delete(request, pk):
    products = get_object_or_404(Basket, pk=pk)
    products.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))