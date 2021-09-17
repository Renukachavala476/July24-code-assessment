from django.urls import path
from .import views

urlpatterns=[
    path('',views.AdminLogin,name="login"),
    path('register',views.AdminRegister,name="register"),
    path('index',views.AdminIndex,name="Index"),
    path('addseller',views.SellerAdd,name="selleradd"),
    path('searchseller',views.Sellersearch,name="search"),
    path('update',views.Sellerupdate,name="updatesearch"),
    path('updateview',views.updatehtml,name="updateview"),
    path('delete',views.SellerDelete,name="delete"),
    path('viewall',views.viewall,name="viewall"),
    path("logout",views.logout,name="logout"),


]