from django.urls import path
from .views import notice_main, free_board, free_board_detail, onenone, onenone_detail


urlpatterns = [
    path('', notice_main),
    path('free/', free_board),
    path('free/<int:id>', free_board_detail),
    path('onenone/', onenone),
    path('onenone/<int:id>', onenone_detail),
]