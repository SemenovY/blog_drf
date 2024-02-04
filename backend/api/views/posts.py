from api.serializers.posts import BlogPostSerializer, BlogSerializer
from api.views.users import get_news_feed_data
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Blog, BlogPost


@extend_schema(
    tags=["Блоги"],
    methods=["GET"],
    description="Блоги пользователей",
)
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@extend_schema(
    tags=["Посты"],
    methods=["POST", "GET", "PUT", "PATCH", "DELETE"],
    description="Посты пользователей",
)
@extend_schema_view(
    perform_create=extend_schema(
        summary="Создать пост",
    ),
    perform_destroy=extend_schema(
        summary="Удалить пост",
    ),
    list_by_user=extend_schema(
        summary="Список постов пользователя",
    ),
    mark_as_read=extend_schema(
        summary="Отметить пост прочитанным",
    ),
)
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        serializer.save(blog=blog)
        page = self.request.query_params.get("page", 1)
        get_news_feed_data(user, page)
        return Response({"detail": "Пост успешно создан."}, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        instance.delete()
        user = instance.user
        page = self.request.query_params.get("page", 1)
        get_news_feed_data(user, page)
        return Response({"detail": "Пост успешно удален."}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["get"])
    def list_by_user(self, request):
        user = self.request.user
        blog = get_object_or_404(Blog, user=user)
        queryset = BlogPost.objects.filter(blog=blog)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def mark_as_read(self, request, pk=None):
        post = self.get_object()
        if request.user != post.user:
            return Response(
                {"detail": "Недостаточно прав для отметки поста как прочитанного."}, status=status.HTTP_403_FORBIDDEN
            )
        post.read = True
        post.save()
        return Response({"detail": "Пост успешно отмечен как прочитанный."}, status=status.HTTP_200_OK)
