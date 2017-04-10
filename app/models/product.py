
from django.db.models import Model, CharField
from django.db.models.fields.related import ManyToManyField
from app.models.tag import Tag

class Product(Model):
    ean = CharField(max_length=20)
    tags = ManyToManyField(Tag, related_name="products")
