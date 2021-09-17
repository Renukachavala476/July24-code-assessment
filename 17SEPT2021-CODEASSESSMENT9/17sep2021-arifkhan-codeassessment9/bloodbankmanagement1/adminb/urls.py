from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    
    path('add/',views.addAdmin,name='addadmin'),
    path('loginadmin/',views.login_check,name='login_checkadmin'),
    path('loginadminview/',views.loginviewadmin,name='loginadminview'),
    path('logoutadmin/',views.logout_admin,name='logout_admin'),


    path('addapi/',views.AddDonor,name='Adddonor'),
    path('register/',views.register,name='register'),

    path('view/',views.viewall,name='viewall'),
    path('viewallapi/',views.Viewdonorall,name='Viewdonorall'),
    path('viewapi/<id>',views.Viewdonor,name='Viewdonor'),

    path('searchview/',views.search_donor,name='search_donor'),
    path('search/',views.searchapi,name='searchapi'),


    path('update/',views.update,name='update'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),


     path('delete_search_api/',views.delete_search_api,name='delete_search_api'),
    path('delete/',views.delete,name='delete'),
    path('delete_api/',views.delete_data_read,name='delete_data_read'),
]