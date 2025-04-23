# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', views.create_user, name='create_user'),
    path('all/', views.get_all_users, name='get_all_users'),
    path('get/<int:pk>/', views.get_user, name='get_user'),
    path('update/<int:pk>/', views.update_user, name='update_user'),
    path('delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('me/', views.get_logged_in_user, name='get_logged_in_user'),
]
