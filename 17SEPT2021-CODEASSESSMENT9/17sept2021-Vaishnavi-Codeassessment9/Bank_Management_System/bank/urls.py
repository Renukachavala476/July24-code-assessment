from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    
    path('add/',views.bankAdmin,name='bankAdmin'),
    path('login/',views.login_check,name='login_checkadmin'),
    path('loginviewbank/',views.loginviewbank,name='loginviewbank'),
    path('logout/',views.logout_bank,name='logout_bank'),


    path('addapi/',views.AddCustomer,name='AddCustomer'),
    path('register/',views.register,name='register'),

    path('view/',views.viewall,name='viewall'),
    path('viewallapi/',views.Viewcustomerall,name='Viewcustomerall'),
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