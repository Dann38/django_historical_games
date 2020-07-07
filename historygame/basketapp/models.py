from django.db import models


from mainapp.models import ProductGame
from authapp.models import GameUser


class Basket(models.Model):
    product = models.ForeignKey(ProductGame, on_delete=models.CASCADE)
    user = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(verbose_name='date_add', auto_now_add=True)

    @property
    def product_cost(self):
        return round(float(self.product.price) * int(self.quantity))

    @property
    def product_pk(self):
        return self.product.pk
