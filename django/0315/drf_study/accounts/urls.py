# accounts/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import example_view


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path('join/', include("dj_rest_auth.registration.urls")),
    # 신기하네.. 얘네 없어도 동작하네
    # path('login/', include("dj_rest_auth.registration.urls")),
    # path('logout/', include("dj_rest_auth.registration.urls")),
    path('test/', example_view),
]