from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()

    context = {"product_list":products}
    return render(request, 'product/product_list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {"product":product}

    return render(request, 'product/product_detail.html', context)