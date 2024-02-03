from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Q

from api.constants import PAGINATION_PAGE_SIZE
from api.serializers.posts import BlogPostSerializer, CustomUserSerializer
from subscriptions.models import Subscription
from users.models import BlogPost, CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=True, methods=['get'])
    def news_feed(self, request, pk=None):
        user = self.get_object()
        page = self.request.query_params.get('page', 1)
        news_feed_data = get_news_feed_data(user, page)
        serializer = BlogPostSerializer(news_feed_data, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='own-posts')
    def own_posts(self, request, pk=None):
        user = self.get_object()
        own_posts = BlogPost.objects.filter(user=user).order_by('-created_at')
        serializer = BlogPostSerializer(own_posts, many=True)
        return Response(serializer.data)


def get_news_feed_data(user, page):
    subscribed_blogs = Subscription.objects.filter(user=user).values_list('blog', flat=True)

    blog_posts = BlogPost.objects.filter(Q(blog__in=subscribed_blogs) & ~Q(user=user)).order_by('-created_at')
    paginator = Paginator(blog_posts, PAGINATION_PAGE_SIZE)
    paginated_blog_posts = paginator.get_page(page)
    return paginated_blog_posts
