
from django.db.models import Model, CharField


class Survey(Model):
    title = CharField(max_length=50)

    def __unicode__(self):
        return self.title
