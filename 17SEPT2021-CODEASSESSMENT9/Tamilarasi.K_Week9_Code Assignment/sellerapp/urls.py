from django.urls import path,include
from .import views

urlpatterns=[

    path('loginadmin1/',views.login_check1,name='login_checkadmin1'),
    path('loginadminview1/',views.loginviewadmin1,name='loginadminview1'),
    path('logoutadmin/',views.logout_admin,name='logout_admin'),

    path('viewallsseller2/',views.myViewAllPage2,name='myViewAllPage2'),
    path('viewall2/',views.mySellerList2,name='mySellerList2'),


    path('viewseller2/<id>',views.mySellerDetails2,name='mySellerDetails2'),
    path('updateread2/',views.UpdateRead2,name='UpdateRead2'),
    path('updatesearch2/',views.UpdateSearchAPI2,name='UpdateSearchAPI2'),
    path('update2/',views.myUpdate2,name='myUpdate2'),
   
]