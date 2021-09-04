from django.urls import path,include
from . import views

urlpatterns = [


    path('fadd/',views.facultyaddpage,name='facultyaddpage'),
    path('viewall/',views.faculty_list,name='faculty_list'),
    path('viewfaculty/<fetchid>',views.faculty_details,name='faculty_details'),
    path('add/',views.faculty_view,name='faculty_view'),
    path('viewfaculty/',views.fac_view,name='fac_view'),
    path('searchfaculty/',views.search_view,name='search_view'),
    path('deletefaculty/',views.delete_view,name='delete_view'),
    path('updatefaculty/',views.update_view,name='update_view'),
    path('search/',views.searchapi,name='searchapi'),
    path('updateactionapi/',views.update_data_read,name='update_data_read'),
    path('updatesearchapi/',views.updatesearchapi,name='updatesearchapi'),
    path('deletesearchapi/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteactionapi/',views.delete_data_read,name='delete_data_read'),
    path('login/',views.login,name='login'),
    path('checklogin/',views.checklogin,name='checklogin'),
    #path('sessions/',views.delete_data_read,name='delete_data_read'),





]