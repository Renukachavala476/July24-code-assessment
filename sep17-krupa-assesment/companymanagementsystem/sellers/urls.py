from django.urls import path, include
from . import views

urlpatterns = [
   

    path('login/', views.loginview, name='loginview'),
    path('viewprofile/', views.profile, name='profile'),
    path('check/', views.login_check, name='login_check'),
    path('registerAction/', views.user_create, name='user_create'),
    path('viewall/', views.viewcustomer, name='viewcustomer'),
    path('view/<fetchid>', views.update_d, name='update_d'),
    path('updatedata/', views.update_data, name='update_data'),





]