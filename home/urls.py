
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    
    path('admin_dashboard', views.adminindex, name="adminindex"),
    path('admin', views.adminlogin, name="admin"),
    path('msg_single', views.msg_single, name="msg_single"),

    path('home', views.index, name="home"),
    path('signup', views.signup, name="signup"),
    path('', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
