from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include('animals.urls')),
    path('admin/', admin.site.urls),
    path('api/reg', include('rest_framework.urls')),


    path('',include('animals.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

