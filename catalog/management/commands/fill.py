import json
from django.db import connection
from django.core.management import BaseCommand
from pathlib import Path

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog.json"), encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_read_products():
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog.json"), encoding='utf-8') as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == 'catalog.product']
        return products

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;')
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(**category['fields']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product['fields']['category'] = Category.objects.get(id=product['fields']['category'])
            product_object = Product(id=product['pk'], **product['fields'])
            product_for_create.append(product_object)

        Product.objects.bulk_create(product_for_create)

