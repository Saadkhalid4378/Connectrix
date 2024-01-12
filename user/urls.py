"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from user.views import home, signup, loginpage

urlpatterns = [
    path('login/', loginpage, name='login'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
]
