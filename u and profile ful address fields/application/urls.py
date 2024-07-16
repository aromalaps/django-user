from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.Home, name='home'),
    path('register/',views.Register, name='register'),
    path('login/',views.Login, name='login'),
    path('logout/',views.Logout,name='logout'),
    path('userprof/<int:id>',views.UserProfiles,name='userprof'),
    path('profile/<int:id>',views.Profiles,name='profile'),
    # path('add_details/',views.UserAddDetails,name='add_detail')
]
 