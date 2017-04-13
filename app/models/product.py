
from django.db.models import Model, CharField
from django.db.models.fields.related import ManyToManyField
from app.models.tag import Tag


class Product(Model):
    ean = CharField(max_length=20)
    name = CharField(max_length=20)
    tags = ManyToManyField(Tag, related_name="products")

    def __unicode__(self):
        return self.name

    def to_json(self):
        res = {
            "ean": self.ean,
            "name": self.name,
            "id": self.id
        }
        return res
