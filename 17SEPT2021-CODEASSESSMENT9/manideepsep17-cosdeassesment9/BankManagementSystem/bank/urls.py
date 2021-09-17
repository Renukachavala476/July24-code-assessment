from django.urls import path,include
from.import views
urlpatterns=[
    path("addcust/",views.addcust,name="addcust"),
    # path("viewevents/",views.veiwallevents,name="viewallevents"),
    path("edit/",views.updatecustomer,name="updatecustomer"),
    path("delete/",views.deletecustomer,name="deletecustomer"),
    path('searchcust/',views.searchcustomer,name='searchcustomer'),



    path('add/',views.addcustomers,name='addcustomers'),
    path('viewall/',views.bank_list,name='bank_list'),
    path('search/',views.searchapi,name='searchapi'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('updateApi/',views.update_data_read,name='update_data_read'),
    path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
    path('deleteApi/',views.delete_data_read,name='delete_data_read'),

    path('view/<fetchid>',views.mycust,name='mycust'),




    path('adminRegistration',views.adminRegistration,name='adminRegistration'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
    path('adminhomepage',views.adminhomepage,name='adminhomepage'),
    path('adminregistrationpage',views.adminregistrationpage,name='adminregistrationpage'),
    path('adminloginpage',views.adminloginpage,name='adminloginpage'),
    path('adminnhome',views.adminnhome,name='adminnhome'),

]

