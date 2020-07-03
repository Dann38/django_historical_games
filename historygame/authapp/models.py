from django.db import models
from django.contrib.auth.models import AbstractUser


class GameUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', default=0)

    @property
    def total_quantity_products(self):
        return sum(map(lambda x: x.quantity, self.basket_set.all()))

    @property
    def purchase_amount(self):
        return sum(map(lambda x: x.product_cost, self.basket_set.all()))
