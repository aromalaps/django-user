from .import views
from django.urls import path

urlpatterns = [
    
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.login,name='Login'),
    path('logout/',views.logout,name='Logout'),
    path('details/<int:id>',views.AddDetails,name='details'),
    path('customer_registration/',views.Customer_registration,name='customer_registration'),
    path('customer_login/',views.Customer_login,name='customer_login'),
    
]