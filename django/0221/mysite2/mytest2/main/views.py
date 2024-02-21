from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("main")

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")
