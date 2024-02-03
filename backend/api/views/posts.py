from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers.posts import BlogPostSerializer, BlogSerializer
from api.views.users import get_news_feed_data
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
        page = self.request.query_params.get('page', 1)
        news_feed_data = get_news_feed_data(user, page)
        serializer = BlogPostSerializer(news_feed_data, many=True)

        return Response(
            {'detail': 'Пост успешно создан.'}, status=status.HTTP_201_CREATED
            )

    def perform_destroy(self, instance):
        instance.delete()

        user = instance.user
        page = self.request.query_params.get('page', 1)
        news_feed_data = get_news_feed_data(user, page)
        serializer = BlogPostSerializer(news_feed_data, many=True)

        return Response(
            {'detail': 'Пост успешно удален.'}, status=status.HTTP_204_NO_CONTENT
            )

    @action(detail=False, methods=['get'])
    def list_by_user(self, request):
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        queryset = BlogPost.objects.filter(blog=blog)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        post = self.get_object()

        if request.user != post.user:
            return Response({'detail': 'Недостаточно прав для отметки поста как прочитанного.'}, status=status.HTTP_403_FORBIDDEN)

        post.read = True
        post.save()

        return Response({'detail': 'Пост успешно отмечен как прочитанный.'}, status=status.HTTP_200_OK)
