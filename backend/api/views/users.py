from rest_framework import generics

from api.serializers.posts import CustomUserSerializer
from users.models import CustomUser


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
