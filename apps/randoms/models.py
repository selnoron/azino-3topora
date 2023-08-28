from django.db import models
from auths.models import MyUser
import os
from django.db.models.manager import Manager


class Banner(models.Model):
    """banner for Reclama"""
    name = models.CharField(
        verbose_name='баннер',
        max_length=20,
    )
    banner_file = models.ImageField(
        verbose_name='файл баннера',
        upload_to='main',
        default='main/unknown.jpeg')
    
    is_active = models.BooleanField(
        verbose_name='активный',
        default=False,
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'баннер'
        verbose_name_plural = 'баннеры'

    def __str__(self) -> str:
        return self.name
    
    def rename_banner_file(self, filename):
        base_path = 'main/'
        extension = filename.split('.')[-1]
        new_filename = f'{self.name}.{extension}'
        return os.path.join(base_path, new_filename)
    

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
    
print(Bet.object.create())