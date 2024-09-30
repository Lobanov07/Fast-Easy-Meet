from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )  # Телефонный номер
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )  # Фото профиля
    preparation_time = models.DurationField(
        default="00:15:00"
    )  # Время на подготовку к созвону
    bio = models.TextField(blank=True, null=True)  # Биография пользователя
    created_at = models.DateTimeField(
        auto_now_add=True)  # Дата создания профиля
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Дата последнего обновления профиля
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="группы",
        blank=True,
        related_name="custom_user_set",  # Укажите уникальное имя
        help_text="Группы, к которым принадлежит пользователь.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="права пользователя",
        blank=True,
        related_name="custom_user_permissions",  # Укажите уникальное имя
        help_text="Разрешения, предоставленные пользователю.",
    )

    # Настройка только для демонстрационных целей
    def __str__(self):
        return self.username  # Может быть изменено на email или другой идентификатор


class Schedule(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="schedules"
    )  # Связь с пользователем
    start_time = models.DateTimeField()  # Время начала
    end_time = models.DateTimeField()  # Время окончания
    description = models.TextField(blank=True, null=True)  # Описание расписания

    class Meta:
        ordering = ["start_time"]  # Сортировка по времени начала


class Meeting(models.Model):
    participants = models.ManyToManyField(
        User, related_name="meetings"
    )  # Участники встречи
    date_time = models.DateTimeField()  # Дата и время встречи
    status = models.CharField(
        max_length=10,
        choices=[
            ("scheduled", "Запланировано"),
            ("completed", "Завершено"),
            ("canceled", "Отменено"),
        ],
        default="scheduled",
    )  # Статус встречи
    agenda = models.TextField(blank=True, null=True)  # Повестка встречи

    def __str__(self):
        return f"Meeting on {self.date_time} with {', '.join([str(participant) for participant in self.participants.all()])}"

    class Meta:
        ordering = ["date_time"]  # Сортировка по времени встречи
