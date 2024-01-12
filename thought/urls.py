
from django.urls import path
from thought import views
urlpatterns = [
    path('thought_detail/<thought_id>/', views.thought_detail, name = 'thought_detail' ),
    path('create_thought/', views.create_thought, name='create_thought'),
]