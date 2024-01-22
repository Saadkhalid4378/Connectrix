
from django.urls import path
from thought import views
urlpatterns = [

    path('update-thought/<pk>/', views.UpdateThought.as_view(), name='update-thought'),
    path('delete-thought/<pk>/', views.DeleteThoughts.as_view(), name='delete-thought'),
    path('users-thoughts/', views.UsersThoughts.as_view(), name='users-thoughts'),

    path('reply-Comment/<id>/', views.reply_Comment, name='reply-Comment'),
    path('thought-detail/<thought_id>/', views.thought_detail, name='thought-detail'),
    path('create-thought/', views.create_thought, name='create-thought'),
    path('share-thought/<int:thought_id>/', views.share_thought, name='share-thought'),

]