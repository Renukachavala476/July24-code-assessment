from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    
    path('add/',views.addmanufacturer,name='addmanufacturer'),
    path('loginmanufacturer/',views.login_check,name='login_checkmanufacturer'),
    path('loginmanufacturerview/',views.loginviewadmin,name='loginmanufacturerview'),
    path('logoutmanufacturer/',views.logout_admin,name='logout_admin'),


    path('addapi/',views.Addseller,name='AddCustomer'),
    path('register/',views.register,name='register'),

    path('view/',views.viewall,name='viewall'),
    path('viewallapi/',views.ViewCustomerall,name='ViewCustomerall'),
    path('viewapi/<id>',views.ViewCustomer,name='ViewCustomer'),

    path('searchview/',views.search_customer,name='search_customer'),
    path('search/',views.searchapi,name='searchapi'),


    path('update/',views.update,name='update'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),


     path('delete_search_api/',views.delete_search_api,name='delete_search_api'),
    path('delete/',views.delete,name='delete'),
    path('delete_api/',views.delete_data_read,name='delete_data_read'),
]