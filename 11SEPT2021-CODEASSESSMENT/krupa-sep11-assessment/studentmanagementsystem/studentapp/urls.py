from django.urls import path, include
from studentapp import views

urlpatterns = [
   

    path('login/', views.loginview, name='loginview'),
    path('register/', views.regview, name='regview'),
   

    path('viewprofile/', views.profile, name='profile'),
    path('check/', views.login_check, name='login_check'),

    path('registerAction/', views.user_create, name='user_create'),



]