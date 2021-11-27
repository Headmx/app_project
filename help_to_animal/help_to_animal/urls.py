from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/', include('animals.urls')),
    path('admin/', admin.site.urls),
    path('api/reg', include('rest_framework.urls')),
]