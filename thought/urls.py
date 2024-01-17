
from django.urls import path
from thought import views
urlpatterns = [
    path('thought_detail/<thought_id>/', views.thought_detail, name = 'thought_detail' ),
    path('create_thought/', views.create_thought, name='create_thought'),
    # path('thought_detail/<pk>/', views.Thought_detail.as_view(), name = 'thought_detail' ),
    path('users_thought/', views.User_thoughts.as_view(), name='users_thought'),
    path('like_thought/<int:pk>', views.like_thought, name='like_thought'),
    # path('comment_thought/<int:pk>', views.Comment_View.as_view(), name='comment_thought'),
]