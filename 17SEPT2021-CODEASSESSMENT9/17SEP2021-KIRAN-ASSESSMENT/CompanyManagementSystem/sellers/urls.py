from django.urls import path,include
from . import views

urlpatterns = [

    path('logincheck/', views.logincheck,name='logincheck'),

    path('loggin/', views.login_Data,name='login_Data'),

    path('addd/', views.addSeller,name='addSeller'),

    path('profile/', views.ProfileData,name='ProfileData'),
    path('PasswordChange/', views.PasswordChange,name='PasswordChange'),

    path('changePassword/', views.MyPasswordChangeView,name='MyPasswordChangeView'),
    #path('PasswordChangedone/', views.MyPasswordResetDoneView,name='MyPasswordResetDoneView'),


  
]