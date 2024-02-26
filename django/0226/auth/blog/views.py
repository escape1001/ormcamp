from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm


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
    if request.method == "POST" :
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect("/blog")
        else : 
            context = {"form": form}
            return render(request, 'blog/create.html', context)
    else :
        form = PostForm()
        context = {"form": form}
        return render(request, 'blog/create.html', context)

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = PostForm(instance=post)
        context = {"form": form, "post":post}
        return render(request, "blog/update.html", context)

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}

    if request.method == "POST" :
        post.delete()
        return redirect("blog_list")
    else :
        return render(request, 'blog/delete.html', context)
