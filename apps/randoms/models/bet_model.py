from django.db import models
from auths.models import MyUser, Transaction
import os
from django.db.models.manager import Manager 


class BetManager(Manager):

    def create(self, **kwargs: dict) -> 'Bet':
        return super().create(**kwargs)


class Bet(models.Model):
    """
    Bet for game!
    """

    class Games(models.TextChoices):
        WHEEL = (0, 'Колесо фартуны')
        SLOT = (1, 'Игровой Автомат')

    game: str = models.CharField(
        verbose_name='игра',
        max_length=200,
        choices=Games.choices
    )
    amout: float = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    who: MyUser = models.ForeignKey(
        verbose_name='кто поставил',
        to=MyUser,
        on_delete=models.CASCADE
    )
    coef: float = models.DecimalField(
        verbose_name='коэффициент',
        max_digits=3,
        decimal_places=1
    )

    object = BetManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

    def win(self) -> None:
        ...

    def lose(self) -> None:
        ...

    def save(self, *args, **kwargs) -> None:
        Transaction.objects.create(
            user=self.who,
            amout=self.amout
        )
        return super().save(*args, **kwargs)
    
    