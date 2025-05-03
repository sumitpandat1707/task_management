from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.get_all_projects, name='get_all_projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:pk>/', views.get_project, name='get_project'),
    path('projects/<int:pk>/update/', views.update_project, name='update_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]
