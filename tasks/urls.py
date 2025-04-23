from django.urls import path
from . import views

urlpatterns = [
    # Task routes
    path('tasks/', views.list_tasks, name='task-list'),                     # GET
    path('tasks/create/', views.create_task, name='task-create'),          # POST
    path('tasks/<int:pk>/', views.retrieve_task, name='task-detail'),      # GET
    path('tasks/<int:pk>/update/', views.update_task, name='update-task'), # PUT
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete-task'), # DELETE
    path('tasks/<int:pk>/update-status/', views.update_task_status, name='update-task-status'),  # PATCH
    path('tasks/user/<int:user_id>/', views.tasks_by_user, name='tasks-by-user'),
]
