from django.contrib import admin
from django.urls import path, include
from tube import views as tubeViews
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tubeViews.tube_list),
    path('tube/', include('tube.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)