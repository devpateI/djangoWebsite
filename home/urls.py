from django.urls import path
from home import views
import sys
urlpatterns = [
    path('', views.index,name='home'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('services',views.services,name='services')
]