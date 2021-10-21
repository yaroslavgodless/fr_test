from django.db import models
from rest_framework import permissions, viewsets

from .models import Questionnaire, Questions
from .serializers import (
    QuestionnaireListSerializer,
    QuestionnaireDetailSerializer,
    AnswerSerializer,
    
)

"""def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
"""
def get_user_id(request):
    current_user = request.user
    return current_user.id


class QuestionnaireViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка опросов"""
    def get_queryset(self):
        questionnaire = Questionnaire.objects.all()
        return questionnaire
    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionnaireListSerializer
        elif self.action == "retrieve":
            return QuestionnaireDetailSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """Ответ на вопрос"""
    def perform_create(self, serializer):
        serializer.save(user_id=get_user_id(self.request))

    def get_queryset(self):
        question = Questions.objects.all()
        return question
    serializer_class = AnswerSerializer


