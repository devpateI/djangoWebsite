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
    path('services',views.services,name='services')
]