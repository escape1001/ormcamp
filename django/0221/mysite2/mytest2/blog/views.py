from django.shortcuts import render
from django.http import HttpResponse

def blog_main(request):
    return HttpResponse("blog_main")

def blog_detail(request, id):
    return HttpResponse(f"blog_detail / {id}")