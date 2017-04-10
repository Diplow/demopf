
from django.db.models import Model, CharField
from django.db.models.fields.related import ManyToManyField
from app.models.tag import Tag


class Survey(Model):
    title = CharField(max_length=50)
    questions = ManyToManyField(Tag, related_name="surveys")
