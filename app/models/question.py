
from django.db.models import Model, CharField, IntegerField
from django.db.models.fields.related import ManyToManyField, ForeignKey
from app.models.tag import Tag
from app.models.survey import Survey


class Question(Model):
    label = CharField(max_length=200)
    tag = ForeignKey(Tag)
    responses = ManyToManyField(Tag, related_name="questions_resp")
    conditions = ManyToManyField(Tag, blank=True, null=True, related_name="questions_cond")

    def __unicode__(self):
        return self.label

    def to_json(self):
        res = {
            "label": self.label,
            "tag": self.tag.to_json(),
            "responses": [resp.to_json() for resp in self.responses.all()]
        }
        return res


class SurveyQuestion(Model):
    position = IntegerField()
    question = ForeignKey(Question, related_name="questions")
    survey = ForeignKey(Survey, related_name="questions")

    def __unicode__(self):
        return self.question.label + "({i})".format(i=self.position)

    def to_json(self):
        res = {
            "position": self.position,
            "question": self.question.to_json(),
            "survey": self.survey.id
        }
        return res
