from rest_framework import serializers

from users.serializers import CustomUserSerializer
from .models import Blog, BlogPost


class BlogPostSerializer(serializers.Serializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogSerializer(serializers.Serializer):
    user = CustomUserSerializer()
    posts = BlogPostSerializer(many=True, read_only=True)


    class Meta:
        model = Blog
        fields = '__all__'
