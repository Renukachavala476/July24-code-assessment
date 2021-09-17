from django.urls import path,include
from .import views

urlpatterns=[
path('logindonor/',views.login_checkdonor,name='login_checkdonor'),
path('login/',views.logindonor,name='logindonor'),
# path('logout/',views.logoutadmin,name='logoutadmin'),
##DONOR OPERATIONS
path('viewallapi/',views.ViewallDonor,name='ViewallDonor'),
path('viewapi/<id>',views.ViewDonor,name='ViewDonor'),
path('viewsdonor/',views.Donorviewall,name='Donorviewall'),
##change password
path('changepassword/',views.changepassword,name='changepassword'),
path('update_api/',views.update_data_read,name='update_data_read'),
path('update_search_api/',views.update_search_api,name='update_search_api'),
##logout
path('logoutdonor/',views.logoutdonor,name='logoutdonor'),

]