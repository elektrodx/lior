"""lior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include, url
from django.conf.urls import patterns, url, include
from django.contrib import admin
from sales.views import Invoice

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^singin/', 'user_lior.views.singin', name='singin'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^add_provider/', 'relations.views.add_provider', name='add_provider'),
    url(r'^add_unit/', 'stock.views.add_unit', name='add_unit'),
    url(r'^add_unit_2/', 'stock.views.add_unit_2', name='add_unit_2'),
    url(r'^add_stock/', 'stock.views.add_stock', name='add_stock'),
    url(r'^list_stock/', 'stock.views.list_stock', name='list_stock'),
    url(r'^list_stock_2/', 'filters.views.list_stock_2', name='list_stock_2'),
    url(r'^list_code/(?P<codegen>\w+)/$', 'filters.views.list_code', name='list_code'),
    url(r'^list_desc/(?P<codi>\w+)/$', 'filters.views.list_desc', name='list_desc'),
    url(r'^add_sucursal/', 'user_lior.views.add_sucursal', name='add_sucursal'),
    url(r'^add_sucursal_2/', 'user_lior.views.add_sucursal_2', name='add_sucursal_2'),
    url(r'^add_sale/', 'sales.views.add_sale', name='add_sale'),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^detail_stock/', 'stock.views.detail_stock', name='detail_stock'),
    url(r'^logout_l/', 'user_lior.views.logout_view', name='logout_view'),
    url(r'^add_shop/', 'shop.views.add_shop', name='add_shop'),
    url(r'^invoice/',  Invoice.as_view()), 
]
