from api.serializers.subscriptions import SubscriptionSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from subscriptions.models import Subscription
from users.models import Blog


@extend_schema(
    tags=["Подписки"],
    methods=["POST", "GET", "DELETE"],
    description="Подписки на авторов",
)
@extend_schema_view(
    create_subscription=extend_schema(
        summary="Подписаться",
    ),
    delete_subscription=extend_schema(
        summary="Отписаться",
    ),
    user_subscriptions=extend_schema(
        summary="Подписки пользователя",
    ),
)
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @action(detail=True, methods=["get"])
    def user_subscriptions(self, request, pk=None):
        user = self.get_object().user if pk is not None else request.user
        subscriptions = Subscription.objects.filter(user=user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def create_subscription(self, request):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog_id = serializer.validated_data["blog_id"]
        blog = get_object_or_404(Blog, id=blog_id)
        subscription, created = Subscription.objects.get_or_create(user=user, blog=blog)
        return Response(serializer.data)

    @action(detail=True, methods=["delete"])
    def delete_subscription(self, request, pk):
        user = self.request.user
        subscription = get_object_or_404(Subscription, pk=pk, user=user)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
