from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addManufacturer,name='addManufacturer'),
    path('addd/', views.addSeller,name='addSeller'),
    path('viewall/', views.viewSeller,name='viewSeller'),
    path('view/<id>', views.sellerDetails,name='sellerDetails'),
    path('search/', views.searchapi,name='searchapi'),
    path('update_search/', views.update_api,name='update_api'),
    path('update/', views.update_dataread,name='update_dataread'),
    path('delete_search/', views.delete_api,name='delete_api'),
    path('delete/', views.delete_dataread,name='delete_dataread'),

    path('login_check/', views.login_check,name='login_check'),

    path('login/', views.loginData,name='loginData'),

    path('sellerpage/', views.SellerAdd,name='SellerAdd'),
    path('sellerviewpage/', views.viewingSeller,name='viewingSeller'),
    path('sellersearchpage/', views.SellerSearch,name='SellerSearch'),
    path('sellereditpage/', views.SellerUpdate,name='SellerUpdate'),
    path('sellerdeletepage/', views.SellerDelete,name='SellerDelete'),


  
]