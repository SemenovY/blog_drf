from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator

from api.constants import MINLENGTHVALIDATOR, TEXT_MAX_LENGTH, TITLE_MAX_LENGTH
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

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


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
    title = models.CharField(max_length=TITLE_MAX_LENGTH, validators=[MinLengthValidator(MINLENGTHVALIDATOR), validate_whitespace])
    text = models.TextField(max_length=TEXT_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.blog == self.user.blog:
            raise ValidationError("You can only post in your own blog.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
