from django.urls import path
from . import views

urlpatterns = [
    path('', views.qna_list, name="qna_list"),
    path('<int:id>/', views.qna_detail, name="qna_detail"),
    path('create/<str:title>/', views.qna_create, name="qna_create"),
    path('delete/<int:id>/', views.qna_delete, name="qna_delete"),
]
