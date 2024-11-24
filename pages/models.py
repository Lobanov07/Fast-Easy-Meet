import uuid

from django.db import models

from accounts.models import CustomUser


class Schedule(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="schedules",
        verbose_name="Пользователь"
    )  # Связь с пользователем
    start_time = models.DateTimeField(
        verbose_name="Время начала"
    )  # Время начала
    end_time = models.DateTimeField(
        verbose_name="Время окончания"
    )  # Время окончания
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )  # Описание расписания

    class Meta:
        ordering = ["start_time"]  # Сортировка по времени начала
        verbose_name = "расписание"
        verbose_name_plural = "Расписания"


class Meeting(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название встречи",
        blank=True,
        null=True,
    )  # Название встречи
    participants = models.ManyToManyField(
        CustomUser,
        related_name="meetings",
        verbose_name="Участники",
        blank=True,
        null=True,
    )  # Участники встречи
    date_time = models.DateTimeField(
        verbose_name="Дата встречи",
        blank=True,
        null=True,
    )  # Дата и время встречи
    preferred_date = models.DateField(
        verbose_name="Предпочтительная дата встречи",
        blank=True,
        null=True,
    )  # Предпочтительная дата встречи
    status = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        choices=[
            ("Запланировано", "Запланировано"),
            ("Завершено", "Завершено"),
            ("Отменено", "Отменено"),
        ],
        default="Неизвестно",
        verbose_name="Статус"
    )  # Статус встречи
    agenda = models.TextField(
        blank=True,
        null=True,
        verbose_name="Повестка встречи"
    )  # Повестка встречи
    unique_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный код"
    )  # Уникальный код встречи
    host = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="hosted_meetings",
        verbose_name="Хост"
    )  # Создатель встречи

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.unique_code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Meeting on {self.date_time} with " + (
               f"{', '.join([str(participant) for participant in self.participants.all()])}")

    class Meta:
        ordering = ["date_time"]
        verbose_name = "встреча"
        verbose_name_plural = "Встречи"
