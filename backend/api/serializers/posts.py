from api.serializers.users import CustomUserSerializer
from rest_framework import serializers
from users.models import Blog, BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = BlogPost
        fields = ["id", "user", "blog", "title", "text", "created_at"]


class BlogSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    posts = BlogPostSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"
