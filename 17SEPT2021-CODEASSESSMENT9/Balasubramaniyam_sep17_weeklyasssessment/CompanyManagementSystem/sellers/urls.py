from django.urls import path
from django.urls import path
from sellers import views

urlpatterns=[
path('',views.login,name="login"),
path("userindex",views.Index,name="index"),
path("changepassword",views.changepassword,name="changepassword"),
path("logout",views.logout,name="logout"),
]