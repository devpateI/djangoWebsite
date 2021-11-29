from django.urls import path
from django.contrib import admin
from home import views
import sys

admin.site.site_header = "Techshop Admin"
admin.site.index_title = "Welcome to Techshop"
admin.site.site_title = "Techshop"
urlpatterns = [
    path('home', views.index,name='home'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('shop',views.shop,name='shop'),
    path('orders',views.orders,name ='orders'),
    path('signin',views.signin,name = 'signin'),
    path('signout',views.signout,name = 'signout'),
]