from django.urls import path
from .views import login, logout

''' URL 구상
    /accounts/login
    /accounts/logout
'''

urlpatterns = [
    path('login/', login),
    path('logout/', logout)
]
