from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Notice
from .serializers import NoticeSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

@extend_schema(
        summary='공지목록',
        description="비회원 R / 회원 RC / 작성자 -",
        request=NoticeSerializer,  # request body의 스키마 지정
        parameters=[
            OpenApiParameter(name='title', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
            OpenApiParameter(name='content', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY)
        ],
    )
@api_view(['GET', 'POST'])
def notice_list(request):
    if request.method == 'GET':
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated :
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = NoticeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errorss, status=status.HTTP_400_BAD_REQUEST)
        

@extend_schema(
        summary='공지상세',
        description="비회원 R / 회원 R / 작성자 RUD",
        request=NoticeSerializer,  # request body의 스키마 지정
        parameters=[
            OpenApiParameter(name='title', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
            OpenApiParameter(name='content', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY)
        ],
    )
@api_view(['GET', 'PUT', 'DELETE'])
def notice_detail(request, pk):
    try :
        notice = Notice.objects.get(pk=pk)
    except Notice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if not request.user.is_authenticated or request.user != notice.author :
            return Response({'message':'수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        if not request.user.is_authenticated or request.user != notice.author :
            return Response(status=status.HTTP_403_FORBIDDEN)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)