from django.urls import path
from .views import BlogListCreateView, BlogPostListCreateView


app_name = "posts"

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blog-posts/', BlogPostListCreateView.as_view(), name='blog-post-list-create')
]
