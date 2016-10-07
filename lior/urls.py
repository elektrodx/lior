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
from django.conf.urls import patterns, url, include
from django.contrib import admin
# from sales.views import Invoice

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^singin/', 'user_lior.views.singin', name='singin'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),    
    url(r'^add_provider/', 'relations.views.add_provider', name='add_provider'),
    url(r'^add_provider_2/', 'relations.views.add_provider_2', name='add_provider_2'),
    url(r'^add_unit/', 'stock.views.add_unit', name='add_unit'),
    url(r'^add_unit_2/', 'stock.views.add_unit_2', name='add_unit_2'),
    url(r'^add_stock/', 'stock.views.add_stock', name='add_stock'),
    url(r'^add_customer/', 'relations.views.add_customer', name='add_customer'),
    url(r'^add_customer_2/', 'relations.views.add_customer_2', name='add_customer_2'),
    url(r'^list_stock/', 'stock.views.list_stock', name='list_stock'),
    url(r'^list_stock_2/', 'filters.views.list_stock_2', name='list_stock_2'),
    url(r'^list_code/(?P<codegen>\w+)/$', 'filters.views.list_code', name='list_code'),
    url(r'^list_desc/(?P<codi>\w+)/$', 'filters.views.list_desc', name='list_desc'),
    url(r'^list_customer/', 'sales.views.list_customer', name='list_customer'),
    url(r'^add_sucursal/', 'user_lior.views.add_sucursal', name='add_sucursal'),
    url(r'^add_sucursal_2/', 'user_lior.views.add_sucursal_2', name='add_sucursal_2'),
    url(r'^add_sale/', 'sales.views.add_sale', name='add_sale'),
    #url(r'^add_sale_2/', 'sales.views.add_sale_2', name='add_sale_2'),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^detail_stock/', 'stock.views.detail_stock', name='detail_stock'),
    url(r'^detail_stock_pag/', 'stock.views.detail_stock_pag', name='detail_stock_pag'),
    url(r'^logout_l/', 'user_lior.views.logout_view', name='logout_view'),
    url(r'^add_shop/', 'shop.views.add_shop', name='add_shop'),
    url(r'^invoice/', 'sales.views.invoice', name='invoice'), 
    # url(r'^list_sales/', 'filters.views.list_sales', name='list_sales'),
    # url(r'^list_detail_sale/(?P<code_sale>\w+)/$', 'filters.views.list_detail_sale', name='list_detail_sale'),
    # url(r'^json_sales/', 'filters.views.json_sales', name='json_sales'),
    # url(r'^json_sale_d/(?P<code_sale_d>\w+)/$', 'filters.views.json_sale_d', name='json_sale_d'),
    # url(r'^add_sale_d/(?P<code_sale_d>\w+)/$', 'sales.views.add_sale_d', name='add_sale_d'),
    # url(r'^add_sale_det/(?P<code_sale_det>\w+)/$', 'sales.views.add_sale_det', name='add_sale_det'),
    # url(r'^sales_savejson/$', 'sales.views.sales_postjson', name='sales_postjson'),
    # url(r'^img_add/', 'admin/img/icon_addlink.gif'),
    url(r'^sales/$', 'sales.views.sale_add', name='sale_add'),
    url(r'^shops/$', 'shop.views.shop_add', name='shop_add'),
    url(r'^eitem/(?P<id>.*)/$', 'stock.views.edit_stock', name='edit_stock'),
    url(r'^report_sale/', 'sales.views.report_sale', name="report_sale"),
    url(r'^report_salew/', 'sales.views.report_salew', name="report_salew"),
    url(r'^report_salem/', 'sales.views.report_salem', name="report_salem"),
    url(r'^search_stock/', 'stock.views.search_stock', name='search_stock'),
    url(r'^add_expenses/', 'assets.views.add_expenses', name='add_expenses'),
    # url(r'^report_exp/', 'assets.views.report_exp', name='report_exp'),
    url(r'^add_price/', 'stock.views.add_price', name='add_price'),
]
