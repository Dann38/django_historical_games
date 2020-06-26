from django.core.management.base import BaseCommand
from mainapp.models import CategoryGame, ProductGame
from authapp.models import GameUser

from django.conf import settings

import json, os


def load_from_json(f_name):
    with open(os.path.join(settings.JSON_PATH, f'{f_name}.json'), encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('category_game')
        CategoryGame.objects.all().delete()
        [CategoryGame.objects.create(**category) for category in categories]

        products = load_from_json('product_game')
        ProductGame.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = CategoryGame.objects.filter(name=category_name).first()
            product['category'] = _category
            ProductGame.objects.create(**product)

        if not GameUser.objects.filter(username='django').exists():
            GameUser.objects.create_superuser(username='django', email='django@geekshop.local', password='geekbrains',
                                              age=33)
