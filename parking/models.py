from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

ROLE = (
    ('Manager', 'Manager'),
    ('Employee', 'Employee'),
)


class Profile(AbstractUser):
    role = models.CharField(verbose_name="Роль", max_length=30, choices=ROLE)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Parking(models.Model):
    parking_number = models.IntegerField(verbose_name='Номер парковки')
    user = models.ForeignKey( Profile, null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name='Пользователь', related_name='user')
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата конца")

    class Meta:
        verbose_name = 'Парковочное место'
        verbose_name_plural = 'Порковочные места'
