from django.urls import path

from . import views
urlpatterns = [
    path('traders', views.traders, name='traders'),
    path('traderadd', views.traderadd, name='traderadd'),
    path('traderdetails',views.trader_details,name='trader_details'),
    #path('vendoradd', views.vendoradd, name='vendoradd'),

    #path('vendor', views.vendor, name='vendor'),
    #path('traderdetails',views.trader_details,name='trader_details'),
    path('buyer_populate', views.buyer_populate, name='buyer_populate'),
    path('seller_populate', views.seller_populate, name='seller_populate'),
    path('trader_populate', views.trader_populate, name='trader_populate'),

    ]