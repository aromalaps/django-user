from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.customer_login, name='customer_login'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff_manager_dashboard/', views.staff_manager_dashboard, name='staff_manager_dashboard'),
    path('delivery_boy_dashboard/', views.delivery_boy_dashboard, name='delivery_boy_dashboard'),
    path('logout/', views.logout, name='logout'),
]
