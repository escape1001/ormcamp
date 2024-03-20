from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('<int:pk>/', views.notice_detail, name='notice_detail'),
]