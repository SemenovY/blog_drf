from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

from api.validation import validate_whitespace


class CustomUser(AbstractUser):
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)

        if created:
            Blog.objects.create(user=self)


class Blog(models.Model):
    """
    Модель блога.

    Attributes:
        user (CustomUser): Пользователь, которому принадлежит блог.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class BlogPost(models.Model):
    """
    Модель поста в блоге.

    Attributes:
        blog (Blog): Блог, к которому относится пост.
        title (str): Заголовок поста.
        text (str): Текст поста.
        created_at (datetime): Время создания поста.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[MinLengthValidator(1), validate_whitespace])
    text = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
