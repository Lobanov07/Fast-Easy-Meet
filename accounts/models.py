from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import timedelta


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Дополнительное поле для описания пользователя
    date_of_birth = models.DateField(blank=True, null=True)  # Поле для даты рождения
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Фото профиля
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )  # Телефонный номер
    preparation_time = models.DurationField(
        default=timedelta(minutes=15)
    )  # Время на подготовку к созвону
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания профиля
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Дата последнего обновления профиля

    def __str__(self):
        return self.username  # Вывод имени пользователя
