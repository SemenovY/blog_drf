from rest_framework import viewsets
from api.serializers.posts import CustomUserSerializer
from users.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
