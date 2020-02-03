
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('vendor_process.urls')),
    path('admin', admin.site.urls),
]