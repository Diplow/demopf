
from django.conf.urls import url

from app.api.views import question, success

urlpatterns = [
    url(r'^question/(?P<survey_id>\d+)/(?P<last_question_position>\d+)$', question),
    url(r'^success/(?P<survey_id>\d+)/(?P<product_id>\d+)$', success)
]
