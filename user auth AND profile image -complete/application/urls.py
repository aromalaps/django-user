from django.shortcuts import render
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('register',views.Register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'), 
    path('image/<int:id>/', views.ProfImage, name='image'),
]
