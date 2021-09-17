from django.urls import path,include
from .import views

urlpatterns=[

    path('loginadmin1/',views.login_check1,name='login_checkadmin1'),
    path('loginadminview1/',views.loginviewadmin1,name='loginadminview1'),
    path('logoutadmin/',views.logout_admin,name='logout_admin'),
    path('viewallcust2/',views.myViewAllPage2,name='myViewAllPage2'),
    path('viewall2/',views.myCustomerList2,name='myCustomerList2'),
    path('logout/',views.logout_admin,name='logout_admin'),



    path('viewseller2/<id>',views.myCustomerDetails2,name='myCustomerDetails2'),
    path('updateread2/',views.UpdateRead2,name='UpdateRead2'),
    path('updatesearch2/',views.UpdateSearchAPI2,name='UpdateSearchAPI2'),
    path('update2/',views.myUpdate2,name='myUpdate2'),
   
]