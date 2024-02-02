from rest_framework import generics
from .models import Blog, BlogPost
from .serializers import BlogSerializer, BlogPostSerializer


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
        blog = Blog.objects.get(user=user)
        serializer.save(blog=blog)
