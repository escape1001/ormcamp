from django.shortcuts import render
from product.models import Product

def main(request):
    products = Product.objects.order_by('-sold_count')[:6]
    context = {"product_top6":products}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')