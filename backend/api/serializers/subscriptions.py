from rest_framework import serializers
#
# from subscriptions.models import Subscription
from users.models import BlogPost
#
#
# class SubscriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         fields = '__all__'
#
#
class NewsFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
