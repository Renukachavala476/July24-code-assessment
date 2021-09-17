from django.urls import path
from . import views

urlpatterns =[
    path('add/',views.addCustomer),
    path('viewall/',views.viewall),
    path('viewcust/',views.viewCust),
    path('view/<id>',views.view),



    path('',views.bank,name='bank'),
    path('updateCustomer/',views.updateCustomer),
    path('deleteCustomer/',views.deleteCustomer),
    path('viewCustomer/',views.viewCustomer),
    path('searchCustomer/',views.searchCustomer),
    path('search/',views.searchapi),
    path('update/',views.update_search),
    path('update_data/',views.update_data,name='update_data'),
    path('delete/',views.delete_search,name="delete_search"),
    path('delete_data/',views.delete_data,name='delete_data'),

    
    path('login/',views.facLogin,name='facLogin'),
    path('custlogin/',views.custLogin,name='custLogin'),
    path('login_check/',views.login_check),
    path('custlogin_check/',views.custlogin_check),
    path('home/',views.home),
    path('custprofile/',views.viewcustProfile),
    


    #####Admin#######
    path('addAdmin/',views.addAdmin),
    
    path('updatecust/',views.update_custsearch),
    path('update_datacust/',views.update_custdata,name='update_data'),
    path('updatecustpwd/',views.updatecustpwd),



    path('custlogout/',views.logout_customer),
    path('adminlogout/',views.logout_admin),
]