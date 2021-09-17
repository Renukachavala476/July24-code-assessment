from django.urls import path,include
from . import views

urlpatterns = [
    path('regiadd/',views.registermanufacturer,name="registermanufacturer"),
    path('regiview/',views.regiview,name="regiview"),
    path('logcheck/',views.login_check,name="login_check"),

    path('regiui/',views.register,name="register"),
    path('logui/',views.login,name="login"),


    path('selleradd/',views.seller_add,name="seller_add"),
    path('sellerview/',views.seller_view,name="seller_view"),
    path('sellerone/<id>',views.sell_viewone,name="sell_viewone"),

    path('selladdui/',views.selleradd,name="selleradd"),
    path('sellviewui/',views.sellerview,name="sellerview"),

    path('sellupdate/',views.sell_update,name="sell_update"),
    path('sellactionupdate/',views.sell_updateaction,name="sell_updateaction"),
    path('updateui/',views.s_update,name="s_update"),

    path('selldelete/',views.delete_seller,name="delete_seller"),
    path('sellactiondel/',views.delete_selleraction,name="delete_selleraction"),
    path('deleteui/',views.s_delete,name="s_delete"),

    #seller#
    path('sellerlogincheck/',views.login_checkseller,name="logincheckseller"),
    
]