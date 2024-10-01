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
    participants = models.ManyToManyField(
        CustomUser,
        related_name="meetings",
        verbose_name="Участники"
    )  # Участники встречи
    date_time = models.DateTimeField(
        verbose_name="Дата встречи"
    )  # Дата и время встречи
    status = models.CharField(
        max_length=10,
        choices=[
            ("scheduled", "Запланировано"),
            ("completed", "Завершено"),
            ("canceled", "Отменено"),
        ],
        default="scheduled",
        verbose_name="Статус"
    )  # Статус встречи
    agenda = models.TextField(
        blank=True,
        null=True,
        verbose_name="Повестка встречи"
    )  # Повестка встречи

    def __str__(self):
        return f"Meeting on {self.date_time} with " + (
               f"{', '.join([str(participant) for participant in self.participants.all()])}")

    class Meta:
        ordering = ["date_time"]  # Сортировка по времени встречи
        verbose_name = "встреча"
        verbose_name_plural = "Встречи"
