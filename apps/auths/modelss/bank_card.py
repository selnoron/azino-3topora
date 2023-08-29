from django.db import models
from django.core.validators import MinValueValidator,RegexValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)  
from django.forms import ValidationError
import datetime
from django.db.models.query import QuerySet
from auths.modelss.my_user import MyUser


class BankCard(models.Model):
    number = models.CharField(
        verbose_name='номер',
        max_length=16,
        validators=[
            RegexValidator(regex=r'^\d{16}$')
        ]
    )
    cvv = models.CharField(
        verbose_name='номер',
        max_length=3,
        validators=[
            RegexValidator(regex=r'^\d{3}$')
        ]
    )
    owner = models.OneToOneField(
        verbose_name='пользователь',
        related_name='card',
        to=MyUser,
        on_delete=models.CASCADE
    )
    experation_time = models.DateField(
        verbose_name='срок действия'
    )
    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Банкоская карта',
        verbose_name_plural = 'Банкоская карты'