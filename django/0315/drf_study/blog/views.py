from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post

@api_view(["GET", "POST", "PUT", "DELETE"])
def blog_list(request):
    if request.method == "GET":
        return Response("hello 1")
    elif request.method == "POST":
        return Response("hello 2")
    elif request.method == "PUT":
        return Response("hello 3")
    elif request.method == "DELETE":
        return Response("hello 4")