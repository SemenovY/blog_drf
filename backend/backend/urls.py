"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import include, path
from users.views import UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
