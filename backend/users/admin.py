"""
Класс администратора для модели CustomUser.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Blog, CustomUser


# class BlogInline(admin.StackedInline):
#     model = Blog
#     can_delete = False
#     verbose_name_plural = 'Blog'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Этот класс расширяет встроенный UserAdmin для дополнительной настройки в административном интерфейсе Django.
    """
    # inlines = (BlogInline,)
    pass
