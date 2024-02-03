from django.db import models

from users.models import Blog, CustomUser


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'blog')
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
