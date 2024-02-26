from django.shortcuts import render
from django.db.models import Q
from .models import Post


def blog_list(request):
    if request.GET.get('q') :
        q = request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=q) | Q(contents__icontains=q)
        ).distinct()
    else :
        posts = Post.objects.all()
        
    context = {"post_list" : posts}
    return render(request, 'blog/blog_list.html', context)

def blog_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'blog/blog_details.html', context)

def create(request):
    context = {}
    return render(request, 'blog/create.html', context)

def update(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'blog/update.html', context)

def delete(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'blog/delete.html', context)
