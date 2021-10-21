from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views, api

urlpatterns = format_suffix_patterns([
    path("questionnaire/", views.QuestionnaireViewSet.as_view({'get': 'list'})),
    path("questionnaire/<int:pk>/", views.QuestionnaireViewSet.as_view({'get': 'retrieve'})),
    path("answer/<int:pk>/", views.AnswerViewSet.as_view({'post': 'create', 'get': 'retrieve'})),
])