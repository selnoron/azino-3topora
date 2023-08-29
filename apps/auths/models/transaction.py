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
from models.my_user import MyUser


class Transaction(models.Model):
    user = models.ForeignKey(
        verbose_name='пользователь',
        related_name='transactions',
        to=MyUser,
        on_delete=models.PROTECT
    )
    amount = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    datetime_created = models.DateField(
        verbose_name='дата транкзации',
        auto_now_add=True,
    )
    is_filled = models.BooleanField(
        verbose_name='пополнение?',
        default=False
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

