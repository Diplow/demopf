
from django.db.models import Model, CharField


class Tag(Model):
    key = CharField(max_length=50)
    value = CharField(max_length=50)
