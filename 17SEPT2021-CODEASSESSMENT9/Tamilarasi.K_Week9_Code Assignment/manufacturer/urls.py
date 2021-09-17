from django.urls import path,include
from .import views

urlpatterns=[

    ############### admin
    path('add/',views.addadmin,name='addadmin'),
    path('loginadmin/',views.login_check,name='login_checkadmin'),
    path('loginadminview/',views.loginviewadmin,name='loginadminview'),
    path('logoutadmin/',views.logout_admin,name='logout_admin'),



    ######Seller
    path('seller1/',views.mySeller,name='mySeller'),
    path('welcomeseller/',views.myWelcomePage,name='myWelcomePage'),
    path('viewallsseller1/',views.myViewAllPage1,name='myViewAllPage1'),
    path('searchseller/',views.mySearch1 ,name='mySearch1'),
    path('update1/',views.myUpdate1,name='myUpdate1'),
    path('delete1/',views.myDelete1,name='myDelete1'),
  
    path('deletesearch1/',views.DeleteSearchAPI1,name='DeleteSearchAPI1'),
    path('deleteread1/',views.DeleteRead1,name='DeleteRead1'),
    path('updateread1/',views.UpdateRead1,name='UpdateRead1'),
    path('updatesearch1/',views.UpdateSearchAPI1,name='UpdateSearchAPI1'),
    path('addseller/',views.mySellerPage,name='mySellerPage'),
    path('viewall1/',views.mySellerList,name='mySellerList'),
    path('viewseller1/<id>',views.mySellerDetails,name='mySellerDetails'),
    path('search1/',views.SearchAPI1,name='SearchAPI1'),
]
