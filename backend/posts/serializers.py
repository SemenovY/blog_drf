from rest_framework import serializers

from users.models import Blog, BlogPost
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    posts = BlogPostSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
