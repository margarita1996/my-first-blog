from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shop_list, name='shop_list'),
    url(r'^shop/(?P<pk>\d+)/$', views.product_list, name='product_list'),
    url(r'^shop/(?P<pk1>\d+)/(?P<pk2>\d+)/$', views.product, name='product'), 
    url(r'^manufacture/(?P<pk>\d+)/$', views.manufacture, name='manufacture'), 
 
    url(r'^filter/$', views.filter, name='filter'),  

    url(r'^filter/findproduct/$', views.findproduct, name='findproduct'),
    url(r'^filter/findproduct/(?P<pk>\d+)/addresses/$', views.addresses, name='addresses'),

    url(r'^filter/findshops/$', views.findshops, name='findshops'),
    url(r'^filter/findshops/(?P<pk>\d+)/products/$', views.products, name='products'),

    url(r'^filter/findshop/$', views.findshop, name='findshop'),

    url(r'^filter/findmanufacture/$', views.findmanufacture, name='findmanufacture'), 

    url(r'^filter/findprice/$', views.findprice, name='findprice'),]