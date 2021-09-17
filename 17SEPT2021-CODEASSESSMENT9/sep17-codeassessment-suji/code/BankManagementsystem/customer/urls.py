from django.urls import path,include
from . import views
urlpatterns=[
    path('addcustomer',views.addcustomer,name='addcustomer'),
    path('customerAddPage',views.customerAddPage,name='customerAddPage'),
]