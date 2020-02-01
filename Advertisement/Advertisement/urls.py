
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path(r'', include('ads.urls')),
    path(r'admin/', admin.site.urls),
]
