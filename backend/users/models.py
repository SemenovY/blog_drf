"""
Кастомный класс пользователя.
"""

from django.contrib.auth.models import AbstractUser

from posts.models import Blog


class CustomUser(AbstractUser):
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)

        if created:
            Blog.objects.create(user=self)
