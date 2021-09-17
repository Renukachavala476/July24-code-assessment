from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manufacturer/',include('manufacturer.urls')),
    path('seller/',include('seller.urls')),
]
