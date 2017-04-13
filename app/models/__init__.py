from tag import Tag
from product import Product
from survey import Survey
from question import Question, SurveyQuestion

from django.contrib import admin

admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(SurveyQuestion)
