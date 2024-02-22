"""
[main]
'www.hojunshopping.com' => 쇼핑몰 소개, 팀 소개, 판매가 많은 상품 6개 소개
'www.hojunshopping.com/about' => 회사 소개

[product]
'www.hojunshopping.com/product' => 상품 목록
'www.hojunshopping.com/product/1'=> 상품 목록 상세 게시물

[qna]
'www.hojunshopping.com/qna' => Q&A 목록
'www.hojunshopping.com/qna/1'=> Q&A 상세 게시물
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('product/', include('product.urls')),
    path('qna/', include('qna.urls')),
]
