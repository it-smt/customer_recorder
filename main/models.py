from django.db import models
from django.utils import timezone

from users.models import User


class Service(models.Model):
    """Модель услуги."""
    name = models.CharField(max_length=256, verbose_name='Наименование')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    duration = models.TimeField(verbose_name='Длительность')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class ContactInformation(models.Model):
    """Модель контактной информации."""
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные информации'

    def __str__(self):
        return f'{self.email} - {self.phone_number}'


class Client(models.Model):
    """Модель клиента."""
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    middle_name = models.CharField(max_length=256, verbose_name='Отчество', blank=True, null=True)
    contact_info = models.ForeignKey(ContactInformation, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()

    def __str__(self):
        return self.get_full_name()


class Record(models.Model):
    """Модель записи клиента."""
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name='Услуга')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Клиент', related_name='records')
    employee = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Мастер', related_name='records')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата и время записи')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.client.last_name} {self.client.first_name} - {self.service.name} ({self.employee.last_name} {self.employee.first_name})'
