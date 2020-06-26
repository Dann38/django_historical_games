from django.db import models
from django.contrib.auth.models import AbstractUser


class GameUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', default=0)


