from rest_framework import generics

from api.serializers.subscriptions import SubscriptionSerializer
from users.models import Subscription


class SubscriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class SubscriptionDeleteView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(user=user)
