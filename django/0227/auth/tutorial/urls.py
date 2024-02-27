"""
1.1 ''                          : 메인페이지
1.1 'blog/'                     : 블로그 글 목록
1.2 'blog/<int:pk>/'            : 블로그 상세 글 읽기
1.3 'accounts/signup/'          : 회원가입
1.4 'accounts/login/'           : 로그인
1.5 'accounts/logout/'          : 로그아웃
1.6 'accounts/profile/'         : 프로필
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]
