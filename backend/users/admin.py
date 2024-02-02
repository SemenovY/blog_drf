"""
Класс администратора для модели CustomUser.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Этот класс расширяет встроенный UserAdmin для дополнительной настройки в административном интерфейсе Django.
    """
    pass
