
from django.urls import path
from . import views
urlpatterns = [
    path('thought_detail/', views.thought_detail, name = 'thought_detail' ),
    path('create_thought/', views.create_thought, name='create_thought'),
]