from django.urls import path,include
from . import views


urlpatterns = [
    
    path('adding/',views.addata,name='addata'),
    path('viewallscreen/',views.viewall,name='viewall'),
    path('searchscreen/',views.searchcode,name='searchcode'),
    path('updatescreen/',views.updation,name='updatation'),
    path('deletescreen/',views.deletion,name='deletion'),
    path('updatescreencus/',views.updationcus,name='updatationcus'),    

#api
    path('add/',views.addcustomer,name='addcustomer'),
    path('viewall/',views.customer_list,name='customer_list'),
    path('viewone/<id>',views.customer_details,name='customer_details'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('updateaction/',views.updatedataread,name='updatedataread'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteaction/',views.deletedataread,name='deletedataread'),


    path('addadmin/',views.addadmin,name='addadmin'),
    path('loginadmin/',views.login_check,name='login_checkadmin'),
    path('loginadminview/',views.loginviewadmin,name='loginadminview'),
    path('logoutadmin/',views.logout_admin,name='logout_admin'),


    path('logincustomer/',views.login_checkcustomer,name='login_checkcustomer'),
    path('logincustomerview/',views.loginviewcustomer,name='loginviewcustomer'),
    path('logoutcustomer/',views.logout_customer,name='logout_customer'),

    path('updatesearchapic/',views.updatesearchapic,name='updatesearchapic'),
    path('updateactionc/',views.updatedatareadc,name='updatedatareadc'),



]

