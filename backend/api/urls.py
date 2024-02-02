from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.posts import BlogViewSet, BlogPostViewSet
from api.views.subscriptions import SubscriptionViewSet
from api.views.users import UserViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog-list-create')
router.register(r'blog-posts', BlogPostViewSet, basename='blog-post-list-create')
router.register(r'subscribe', SubscriptionViewSet, basename='subscription-create')
router.register(r'unsubscribe', SubscriptionViewSet, basename='subscription-delete')
router.register(r'users', UserViewSet, basename='user-detail')

urlpatterns = [
    path("v1/", include(router.urls)),
]
