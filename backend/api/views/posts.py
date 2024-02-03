from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers.posts import BlogPostSerializer, BlogSerializer
from users.models import Blog, BlogPost


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        serializer.save(blog=blog)

    @action(detail=False, methods=['get'])
    def list_by_user(self, request):
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        queryset = BlogPost.objects.filter(blog=blog)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
