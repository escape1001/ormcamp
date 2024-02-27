from django.shortcuts import render

def blog_list(request):
    context = {}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    context = {"pk":pk}
    return render(request, 'blog/blog_detail.html', context)