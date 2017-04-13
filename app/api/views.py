
from django.http import HttpResponse

from app.models import SurveyQuestion, Question, Tag, Survey, Product
from app.recommendation.base import getRecommendation

import json

def question(request, survey_id, last_question_position):
    questions = SurveyQuestion.objects.filter(survey=survey_id, position__gt=last_question_position)
    profile = [int(tag) for tag in request.GET["tags"].split(',')] if "tags" in request.GET else []
    for question in questions:
        unmet_conditions = 0
        for condition in question.question.conditions.all():
            if condition.id not in profile:
                unmet_conditions += 1
                break
        if unmet_conditions == 0:
            return HttpResponse(json.dumps(question.to_json()))
    recommendation = getRecommendation(profile)
    return HttpResponse(recommendation)


def success(request, survey_id, product_id):
    pass
        
            
