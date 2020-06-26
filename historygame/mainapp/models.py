from django.db import models


class CategoryGame (models.Model):
    name = models.CharField(verbose_name='категории', max_length=64)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class ProductGame(models.Model):
    category = models.ForeignKey(CategoryGame, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(verbose_name='название игры', max_length=128)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена', decimal_places=2, max_digits=8, default=0)
    image = models.ImageField(verbose_name='картинка', upload_to='games_images', blank=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'