from django.urls import path
from .views import qna_list, qna_detail


urlpatterns = [
    path('', qna_list),
    path('<int:id>', qna_detail),
]