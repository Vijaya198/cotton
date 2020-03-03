
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('account_login.urls')),

    path('', include('trade_information.urls')),
    # path('account_login/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]