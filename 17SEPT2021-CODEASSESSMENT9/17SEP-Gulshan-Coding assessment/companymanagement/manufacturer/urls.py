from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin 


urlpatterns=[ 

    path('manucheck/', views.manucheck, name='usercheck'),
    path('dashboard/', views.cusDashboard, name='cusDashboard'),
    path('myaccount/', views.customerprofile, name='myaccount'),
    path('manu/', views.Manufacturer, name='myaccount'),

    path('usercheck/', views.usercheck, name='usercheck'),
    path('myaccount', views.CustomerValidation, name='cusDashboard'),
    path('deleteapi/', views.deleteapi, name='myaccount'),
    path('deletedata/', views.delete_data, name='myaccount'),
    path('dashboard', views.dashboard, name='myaccount'),





]