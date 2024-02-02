from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers.subscriptions import SubscriptionSerializer
from subscriptions.models import Subscription
from users.models import Blog


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @action(detail=True, methods=['get'])
    def user_subscriptions(self, request, pk=None):
        # Получаем пользователя по его идентификатору
        user = self.get_object().user if pk is not None else request.user
        subscriptions = Subscription.objects.filter(user=user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_subscription(self, request):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog_id = serializer.validated_data['blog_id']
        blog = get_object_or_404(Blog, id=blog_id)
        subscription, created = Subscription.objects.get_or_create(user=user, blog=blog)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def delete_subscription(self, request, pk):
        user = self.request.user
        subscription = get_object_or_404(Subscription, pk=pk, user=user)
        subscription.delete()
        return Response(status=204)
