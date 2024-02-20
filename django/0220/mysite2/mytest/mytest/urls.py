"""
URL configuration for mytest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main.views import index, notice, notice_detail, contact, abcd, user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('notice/', notice),
    re_path(r'^notice/(?P<id>[1-3])/$', notice_detail),
    # path('notice/<int:id>', notice_detail),
    path('contact/', contact),
    path('a/b/c/d/', abcd),
    path('user/<str:username>', user),
]
