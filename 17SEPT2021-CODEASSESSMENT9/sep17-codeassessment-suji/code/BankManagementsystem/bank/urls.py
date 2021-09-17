from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.AddPage,name='AddPage'),
    path('bsignin',views.bsignin,name='bsignin'),
    
  
]