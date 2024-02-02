from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.posts import BlogViewSet, BlogPostViewSet
from api.views.subscriptions import SubscriptionViewSet
from api.views.users import UserViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog-list-create')
router.register(r'blog-posts', BlogPostViewSet, basename='blog-post-list-create')
router.register(r'users', UserViewSet, basename='user-detail')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/users/<int:pk>/subscriptions/", SubscriptionViewSet.as_view({'get': 'user_subscriptions'}), name='user-subscription-list'),
]
