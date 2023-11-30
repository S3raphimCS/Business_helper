from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# class Employee(models.Model):
#     user = models.ForeignKey(
#         get_user_model(),
#     )

# class File(models.Model):
#     file = models.FileField(
#         _("Файл"),
#     )
#
#     def __str__(self):
#         return self.file.name
#
#     class Meta:
#         verbose_name = "Файл"
#         verbose_name_plural = "Файлы"


# Потенциально можно добавить область
class City(models.Model):
    """Модель города России для создания объектов"""
    name = models.CharField(
        _("Наименование города"),
        max_length=50,
        blank=True, null=False,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class WorkObject(models.Model):
    """Модель рабочего объекта"""
    title = models.CharField(
        _("Название"),
        max_length=100,
    )
    street = models.CharField(
        _("Улица"),
        max_length=100,
        blank=True, null=True
    )
    workers = models.ManyToManyField(
        get_user_model(),
        _("Сотрудники"),
        blank=True,
    )

    def __str__(self):
        return f"{self.street}: {self.title}"

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class Task(models.Model):
    """Модель постановки задачи"""
    COMPLETING = 'completing'
    ADJUSTMENT = 'adjustment'
    REVIEW = 'review'
    IN_AGREEMENT = 'in agreement'
    COMPLETED = 'completed'

    CHOICE_STATUS = (
        (COMPLETING, 'На выполнении'),
        (REVIEW, "На проверке"),
        (ADJUSTMENT, 'На корректировке'),
        (IN_AGREEMENT, "На согласовании"),
        (COMPLETED, "Выполнена"),
    )

    object = models.ForeignKey(
        WorkObject,
        on_delete=models.CASCADE,
        verbose_name=_("Объект"),
    )
    title = models.CharField(
        _("Название"),
        max_length=100,
        null=False, blank=True
    )
    description = models.TextField(
        _("Описание"),
        null=True, blank=True
    )
    stater = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Постановщик"),
        on_delete=models.SET_NULL,
        null=True,
    )
    responsible = models.ManyToManyField(
        get_user_model(),
        verbose_name="Выполняющие",
        related_name="responsible_workers",
        blank=True,
    )
    state = models.CharField(
        _("Статус задачи"),
        choices=CHOICE_STATUS,
        max_length=30,
    )
    result = models.FileField(
        _("Файл"),
        blank=True, null=True
    )
    start_date = models.DateTimeField(
        _("Дата постановки"),
        auto_now_add=True,
    )
    deadline = models.DateTimeField(
        _("Дедлайн"),
    )

    def __str__(self):
        return f"{self.object.title}: {self.title}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
