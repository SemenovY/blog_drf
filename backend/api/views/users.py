from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from api.paginations import NewsFeedPagination
from api.serializers.posts import CustomUserSerializer
from api.serializers.subscriptions import NewsFeedSerializer
from users.models import BlogPost, CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=True, methods=['get'])
    def news_feed(self, request, pk=None):
        user = self.get_object()
        page = self.request.query_params.get('page', 1)
        news_feed_data = get_news_feed_data(user, page)
        serializer = NewsFeedSerializer(news_feed_data, many=True)
        return Response(serializer.data)


def get_news_feed_data(user, page):
    subscribed_blogs = user.subscriptions.all()
    blog_posts = BlogPost.objects.filter(blog__in=subscribed_blogs).order_by('-created_at')
    paginator = NewsFeedPagination()
    paginated_blog_posts = paginator.paginate_queryset(blog_posts, page)
    return paginated_blog_posts
