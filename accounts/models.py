from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import timedelta


class CustomUser(AbstractUser):
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="Биография"
    )  # Дополнительное поле для описания пользователя
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения"
    )  # Поле для даты рождения
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
        verbose_name="Фото профиля"
    )  # Фото профиля
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона"
    )  # Телефонный номер
    preparation_time = models.DurationField(
        default=timedelta(minutes=15),
        verbose_name="Время на подготовку"
    )  # Время на подготовку к созвону
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Профиль создан"
    )  # Дата создания профиля
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Профиль обновлен"
    )  # Дата последнего обновления профиля

    def __str__(self):
        return self.username  # Вывод имени пользователя

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "пользователи"
