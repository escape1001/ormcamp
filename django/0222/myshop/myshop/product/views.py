from django.shortcuts import render

def product_list(request):
    return render(request, 'product/product_list.html')


def product_detail(request, id):
    context = {
        "id" : id
    }

    return render(request, 'product/product_detail.html', context)