"""
# urls 기획
1. 다음 url이 실제 작동하도록 해주세요.
1.1 'blog/'                     : 블로그 글 목록
1.2 'blog/<int:pk>/'            : 블로그 글 읽기
1.3 'blog/create/'              : 블로그 글 작성
1.4 'blog/update/<int:pk>/'     : 블로그 글 업데이트
1.5 'blog/delete/<int:pk>/'     : 블로그 글 삭제

###################################
앱이름: blog                views 함수이름   html 파일이름  비고
'blog/'                     blog            blog.html    
'blog/<int:pk>'             post            post.html
'blog/create/'              create          create.html
'blog/update/<int:pk>/'     update          update.html
'blog/delete/<int:pk>/'     delete          delete.html

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('<int:pk>/', views.blog_details, name="blog_details"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
