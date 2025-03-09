from django.contrib.auth import views as auth_views
from django.urls import path
from .views import  CustomLoginView
from . import views
from .views import *

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('accounts/password_change/', views.password_change, name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #password reset
    path('accounts/password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='app/users/password_reset.html'), 
         name='password_reset'),

    # path('accounts/password_reset/done/', 
    #      auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
    #      name='password_reset_done'),

    # path('accounts/reset/<uidb64>/<token>/', 
    #      auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
    #      name='password_reset_confirm'),

    # path('accounts/reset/done/', 
    #      auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
    #      name='password_reset_complete'),
]
