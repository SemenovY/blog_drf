from django.db import models

from users.models import CustomUser
from django.core.validators import MinLengthValidator


class Blog(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[MinLengthValidator(
        1)])
    text = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
