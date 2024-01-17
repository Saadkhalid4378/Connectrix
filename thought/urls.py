
from django.urls import path
from thought import views
urlpatterns = [
    path('user_thought/', views.User_thought.as_view(), name = 'user_thought' ),
    path('users_thought/', views.Users_thoughts.as_view(), name='users_thought'),
    path('thought_detail/<thought_id>/', views.thought_detail, name = 'thought_detail' ),
    path('create_thought/', views.create_thought, name='create_thought'),
    path('like_thought/<int:pk>', views.like_thought, name='like_thought'),
]