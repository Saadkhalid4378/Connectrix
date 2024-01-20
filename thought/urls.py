
from django.urls import path
from thought import views
urlpatterns = [
    # path('user_thought/', views.User_thought.as_view(), name = 'user_thought' ),
    path('users_thoughts/', views.UsersThoughts.as_view(), name='users_thoughts'),
    
    path('replyComment/<id>/', views.reply_Comment, name='replyComment'),
    path('thought_detail/<thought_id>/', views.thought_detail, name = 'thought_detail' ),
    path('create_thought/', views.create_thought, name='create_thought'),
    # path('like_thought/<int:pk>', views.like_thought, name='like_thought'),
    # path('comment_thought/<int:pk>', views.Comment_View.as_view(), name='comment_thought'),
]