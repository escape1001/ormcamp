from django.contrib import admin
from django.urls import path, include

''' URL 구상
    /
    /about
    /contact

    /accounts/login
    /accounts/logout

    /accounts/blog
    /accounts/blog/1
    /accounts/blog/2
    /accounts/blog/3
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")), # "" URL로 들어오면 main 앱에 있는 urls.py로 연결하겠다.
    path('blog/', include("blog.urls")), # "blog" URL로 들어오면 blog 앱에 있는 urls.py로 연결하겠다.
    path('accounts/', include("accounts.urls")), # "accounts" URL로 들어오면 accounts 앱에 있는 urls.py로 연결하겠다.
]
