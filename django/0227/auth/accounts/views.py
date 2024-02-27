from django.shortcuts import render

def signup(request):
    context = {}
    return render(request, 'accounts/signup.html', context)

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def logout(request):
    context = {}
    return render(request, 'accounts/logout.html', context)

def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)
