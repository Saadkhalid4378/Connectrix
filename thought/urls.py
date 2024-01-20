
from django.urls import path
from thought import views
urlpatterns = [

    path('delete-thought/<pk>/', views.DeleteTHoughts.as_view(), name='delete-thought'),
    path('users-thoughts/', views.UsersThoughts.as_view(), name='users-thoughts'),
    path('reply-Comment/<id>/', views.reply_Comment, name='reply-Comment'),
    path('thought-detail/<thought_id>/', views.thought_detail, name = 'thought-detail' ),
    path('create-thought/', views.create_thought, name='create_thought'),
    path('share-thought/<int:thought_id>/', views.share_thought, name='share-thought'),

]