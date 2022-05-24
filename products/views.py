from django.shortcuts import render

from .models import Product


def home_view(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home-page.html', context)


def order_product(request):
    return render(request, 'product-page.html')


def order_checkout(request):
    return render(request, 'checkout-page.html')

