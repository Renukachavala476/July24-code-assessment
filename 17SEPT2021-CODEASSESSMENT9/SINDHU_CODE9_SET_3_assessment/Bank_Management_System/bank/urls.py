from django.urls import path,include
from . import views
urlpatterns = [
    #####BANK PAGE
    path('add/',views.bank_create,name='bank_create'),
    path('loginadmin/',views.login_check,name='login_checkadmin'),
    path('loginadminview/',views.loginviewadmin,name='loginadminview'),


    ####
    #views
    path('reg/',views.add_customer_view,name='add_customer_view'),
    path('searchview/',views.search_customer_view,name='search_customer_view'),
    path('viewupdate/',views.update_customer_view,name='update_customer_view'),
    path('viewdelete/',views.delete_customer_view,name='delete_customer_view'),
    path('viewallcustomer/',views.viewall_customer_view,name='viewall_customer_view'),
    ####
    path('addcustomer/',views.customer_create,name='customer_create'),
    path('view/<id>',views.customer_details,name='customer_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('update_action_api/',views.update_data_read,name='update_data_read'),
    path('updatesearch/',views.updateapi,name='updateapi'),
    path('deletesearch/',views.deleteapi,name='deleteapi'),
    path('delete_action_api/',views.delete_data_read,name='delete_data_read'),
    path('viewall/',views.customer_list,name='customer_list'),
    
]