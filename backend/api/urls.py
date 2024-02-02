from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.posts import BlogListCreateView, BlogPostListCreateView
from api.views.subscriptions import SubscriptionCreateView, \
    SubscriptionDeleteView
from api.views.users import UserDetailView

app_name = "api"

router = DefaultRouter()
router.register(r'blogs', BlogListCreateView, basename='blog-list-create')
router.register(r'blog-posts', BlogPostListCreateView, basename='blog-post-list-create')
router.register(r'subscribe', SubscriptionCreateView, basename='subscription-create')
router.register(r'unsubscribe', SubscriptionDeleteView, basename='subscription-delete')


urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path("v1/", include(router.urls)),

]
