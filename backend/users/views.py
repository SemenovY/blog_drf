from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import CustomUserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
