from django.urls import path,include
from .import views
urlpatterns = [
    
    path('',views.Home,name="home"),
    path('displ/',views.Display,name="output"),
    path('update/<int:id>',views.Update,name="update"),
    path('delete/<int:id>',views.Delete,name="delete")


    
] 