from django.db.models import Model, ForeignKey, CASCADE, FloatField
from django.db.models import CharField


class Category(Model):
    name = CharField(max_length=20)


class Product(Model):
    name = CharField(max_length=20)
    price = FloatField()
    category = ForeignKey('apps.Category', CASCADE, related_name='product')



