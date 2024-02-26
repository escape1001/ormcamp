from django.shortcuts import render

def main(request):
    print(request)
    print(request.GET)
    return render(request, "main/index.html")