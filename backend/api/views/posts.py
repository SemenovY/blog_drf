from django.shortcuts import get_object_or_404
from rest_framework import generics

from api.serializers.posts import BlogPostSerializer, BlogSerializer
from users.models import Blog, BlogPost


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        """
        Получаем текущего пользователя и связанный блог.
        """
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        serializer.save(blog=blog)

    def get_queryset(self):
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        from django.shortcuts import get_list_or_404
        return get_list_or_404(BlogPost, blog=blog)
