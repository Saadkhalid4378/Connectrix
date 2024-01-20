"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from user.views import home, signup, login_page, logout_user
from user.views import ProfileView, EditProfile

urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    
    path('edit_profile/<pk>/', EditProfile.as_view(), name='edit_profile'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
    # path('home/', Home.as_view(), name='home'),
]