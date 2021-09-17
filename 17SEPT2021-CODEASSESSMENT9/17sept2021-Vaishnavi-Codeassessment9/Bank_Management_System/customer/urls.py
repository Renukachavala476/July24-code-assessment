from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

path('logincheck/',views.loginCheck,name='logincheck'),
path('loginview/',views.loginview,name='loginview'),

path('viewapi/<id>',views.ViewDonor,name='ViewCustomer'),

path('update/',views.update,name='update'),
path('update_api/',views.update_data_read,name='update_data_read'),
path('update_search_api/',views.update_search_api,name='update_search_api'),
   


    
]