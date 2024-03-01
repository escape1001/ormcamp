from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import PostSerializer

'''
def blog_list(request): 
    # queryset은 못담아보냄
    posts = Post.objects.all()
    data = {"posts": posts}

    # 방법 1 : 리스트로 만들어서 반환하거나
    posts = []
    for i in Post.objects.all():
        posts.append({'title':i.title, 'content':i.content})

    # 방법 2 : posts를 순회해가면서 각각의 값을 딕셔너리로 만들어서 반환
    (다소 노가다)
    return JsonResponse(posts, safe=False) # dictionary이외를 받을 경우, safe=False
'''


# FBV 사용하는 방식
@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True) # 다수의 Queryset을 넘길 때는 many=True
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)