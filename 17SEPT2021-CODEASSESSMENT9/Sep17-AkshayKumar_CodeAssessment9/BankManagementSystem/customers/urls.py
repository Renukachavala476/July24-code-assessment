from django.urls import path
from . import views

urlpatterns =[
    
    path('viewcust/',views.viewCust),
    




    
 
    path('custlogin/',views.custLogin,name='custLogin'),
    
    path('custlogin_check/',views.custlogin_check),
 
    path('custprofile/',views.viewcustProfile),
    



    
    path('updatecust/',views.update_custsearch),
    path('update_datacust/',views.update_custdata,name='update_data'),
    path('updatecustpwd/',views.updatecustpwd),



    path('custlogout/',views.logout_customer),
    path('adminlogout/',views.logout_admin),
]