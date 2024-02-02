from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.serializers import BlogSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    blog = BlogSerializer()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'blog']
