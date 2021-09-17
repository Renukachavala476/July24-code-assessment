from django.urls import path,include
from .import views

urlpatterns=[
path('add/',views.addadmin,name='addadmin'),
path('loginadmin/',views.login_checkadmin,name='login_checkadmin'),
path('login/',views.loginadminview,name='loginadminview'),
path('logout/',views.logoutadmin,name='logoutadmin'),

##DONOR ADD##
path('addapi/',views.AddDonor,name='AddDonor'),
path('register/',views.DonorAdd,name='DonorAdd'),
##DONOR VIEW
path('viewallapi/',views.ViewallDonor,name='ViewallDonor'),
path('viewapi/<id>',views.ViewDonor,name='ViewDonor'),
path('views/',views.Donorviewall,name='Donorviewall'),
##DONOR SEARCH
path('searchview/',views.search_donor,name='search_donor'),
path('search/',views.searchapi,name='searchapi'),
##DONOR UPDATE
path('update/',views.update,name='update'),
path('update_api/',views.update_data_read,name='update_data_read'),
path('update_search_api/',views.update_search_api,name='update_search_api'),
##DONOR DELETE
path('delete_search_api/',views.delete_search_api,name='delete_search_api'),
path('delete/',views.delete,name='delete'),
path('delete_api/',views.delete_data_read,name='delete_data_read'),
]