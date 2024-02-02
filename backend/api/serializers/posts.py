from rest_framework import serializers

from api.serializers.users import CustomUserSerializer
from users.models import Blog, BlogPost


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
