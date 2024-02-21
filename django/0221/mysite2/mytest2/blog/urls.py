from django.urls import path
from .views import blog_main, blog_detail

''' URL 구상
    /accounts/blog
    /accounts/blog/1
    /accounts/blog/2
    /accounts/blog/3
'''

urlpatterns = [
    path('', blog_main),
    path('<str:id>/', blog_detail)
]
