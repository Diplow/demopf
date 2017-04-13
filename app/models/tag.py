
from django.db.models import Model, CharField
from django.db.models.fields.related import ForeignKey


class Tag(Model):
    key = ForeignKey("self", blank=True, null=True)
    value = CharField(max_length=50)
    ordering = ('key', 'value')

    def __unicode__(self):
        if self.key is None:
            return self.value
        else:
            return unicode(self.key) + ": " + self.value

    def to_json(self):
        res = {
            "key": self.key.to_json() if self.key is not None else "",
            "value": self.value,
            "id": self.id
        }
        return res
