from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import generate_secret_token


class PersonalInformation(models.Model):
    """Модель личной информации."""
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
    passport = models.CharField(max_length=50, verbose_name='Паспорт')
    address = models.CharField(max_length=256, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Персональная информация'
        verbose_name_plural = 'Персональные информации'

    def __str__(self):
        return f'{self.phone_number} - {self.address}'


class WorkingDay(models.Model):
    """Модель рабочего дня."""
    day = models.CharField(max_length=50, verbose_name='День недели')
    shift_start_time = models.TimeField(verbose_name='Время начала смены')
    shift_end_time = models.TimeField(verbose_name='Время окончания смены')

    class Meta:
        verbose_name = 'Рабочий день'
        verbose_name_plural = 'Рабочие дни'

    def __str__(self):
        return f'{self.day} ({self.shift_start_time} - {self.shift_end_time})'


class User(AbstractUser):
    """Кастомная модель пользователя."""

    class Gender(models.TextChoices):
        MALE = 'Мужской', 'Мужской'
        FEMALE = 'Женский', 'Женский'

    auth_token = models.CharField(max_length=256, verbose_name='Секретный токен')
    middle_name = models.CharField(max_length=256, verbose_name='Отчество', blank=True, null=True)
    age = models.IntegerField(verbose_name='Возраст', default=1)
    gender = models.CharField(max_length=7, choices=Gender.choices, default=Gender.MALE, verbose_name='Пол')
    personal_information = models.ForeignKey(PersonalInformation, on_delete=models.PROTECT,
                                             verbose_name='Персональная информация', blank=True, null=True)
    working_days = models.ManyToManyField(WorkingDay, verbose_name='Рабочие дни', blank=True, null=True)
    is_master = models.BooleanField(default=False, verbose_name='Мастер')

    def save(self, *args, **kwargs):
        self.auth_token = generate_secret_token()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.username}'
