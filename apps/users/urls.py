from django.contrib.auth import views as auth_views
from django.urls import path
from .views import  CustomLoginView
from . import views
from .views import *

urlpatterns = [
    path('accounts/password_change/', views.password_change, name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('accounts/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]
