"""Defines url patterns for users."""
from django.conf.urls import url
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,login,authenticate
from . import views
app_name = 'users'
LoginView.template_name = 'users/login.html'
urlpatterns = [
    # Login page.
    path('users/login/', LoginView.as_view(), name='login'),
        
    # Logout page.
    path('logout/', views.logout_view, name='logout'),
    
    # Registration page. 
    path('register/', views.register, name='register'),
]
