from django.urls import path,include
from .import views

urlpatterns = [
    path('selluilogin/',views.sellerlogin,name="sellerlogin"),
    path('selluiprofile/',views.sellerprofile,name="sellerprofile"),
]