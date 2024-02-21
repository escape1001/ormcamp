from django.shortcuts import render

def product_list(request):
    return render(request, 'product/index.html')

def product_detail(request, id):
    return render(request, 'product/product_detail.html', {"id":id})
