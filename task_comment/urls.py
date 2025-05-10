from django.urls import path
from . import views

urlpatterns = [
    path('comments/task/<int:task_id>/', views.get_comments_by_task, name='get_comments_by_task'),
    path('comments/add/', views.add_comment, name='add_comment'),
    path('comments/update/<int:pk>/', views.update_comment, name='update_comment'),
    path('comments/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comments/<int:task_id>/latest/', views.get_latest_comment_by_task, name='latest-comment'),
    
]
