from django.urls import path,include
from . import views

urlpatterns = [
   #VIEWS
    path('add/',views.donor_view,name='donor_view'),
    path('viewdonor/',views.don_view,name='don_view'),
    path('updatedonor/',views.upd_view,name='upd_view'),
    path('deletedonor/',views.del_view,name='del_view'),
    path('searchdonor/',views.search_view,name='search_view'),

    #APIS
    path('dadd/',views.donoraddpage,name='donoraddpage'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('viewall/',views.donor_list,name='donor_list'),
    path('viewemployee/<fetchid>',views.donor_details,name='donor_details'),
    path('updateactionapi/',views.update_data_read,name='update_data_read'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteactionapi/',views.delete_data_read,name='delete_data_read'),
   
]