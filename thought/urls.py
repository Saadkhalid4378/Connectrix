
from django.urls import path
from thought import views
urlpatterns = [
    # path('user_thought/', views.User_thought.as_view(), name = 'user_thought' ),
    path('replyComment/<id>/', views.replyComment, name='replyComment'),
    path('users_thoughts/', views.Users_thoughts.as_view(), name='users_thoughts'),
    path('thought_detail/<thought_id>/', views.thought_detail, name = 'thought_detail' ),
    path('create_thought/', views.create_thought, name='create_thought'),
    # path('like_thought/<int:pk>', views.like_thought, name='like_thought'),
    # path('comment_thought/<int:pk>', views.Comment_View.as_view(), name='comment_thought'),
]