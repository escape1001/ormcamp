""" 앱 설계
    쇼핑몰을 만들 예정입니다. 쇼핑몰에 만들 url 목록은 아래와 같습니다. 
    적절한 앱으로 나눠 설계하고 Django로 코딩해주세요.

    1. 설계한 파일은 코드블록으로 올려주세요.
    2. 접속이 제대로 되는지 product/1, notice/free/1, notice/onenone/1 3개를 캡쳐(이미지)해 올려주세요.

    'www.hojunshopping.com' => 잘 나가는 상품 10개 소개
    'www.hojunshopping.com/about' => 회사 소개
    'www.hojunshopping.com/contact' => 오시는 길

    'www.hojunshopping.com/product' => 상품 목록
    'www.hojunshopping.com/product/1'=> 상품 목록 상세 게시물
    
    'www.hojunshopping.com/qna' => Q&A 목록
    'www.hojunshopping.com/qna/1'=> Q&A 상세 게시물
    
    'www.hojunshopping.com/notice' => 자유게시판, 1:1게시판 선택 페이지
    'www.hojunshopping.com/notice/free' => 자유게시판 목록
    'www.hojunshopping.com/notice/free/1' => 자유게시판 상세 게시물
    'www.hojunshopping.com/notice/onenone' => 1:1 상담 안내
    'www.hojunshopping.com/notice/onenone/1'  => 1:1 상담 상세 게시물

    앱이름:         
    URL주소     views 함수이름      html 파일이름       비고
    ''        
    'about/'        
    ... 생략 ...

    앱이름:         
    URL주소     views 함수이름      html 파일이름       비고
    ''        
    'about/'        
    ... 생략 ...

    앱이름:         
    URL주소     views 함수이름      html 파일이름       비고
    ''        
    'about/'        
    ... 생략 ...
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('product/', include("product.urls")),
    path('qna/', include("qna.urls")),
    path('notice/', include("notice.urls")),
]
