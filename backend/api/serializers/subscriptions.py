from rest_framework import serializers

from api.serializers.posts import BlogSerializer
from api.serializers.users import CustomUserSerializer
from subscriptions.models import Subscription
from users.models import BlogPost


class SubscriptionSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    blog = BlogSerializer()

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'blog']


class NewsFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
