from django.shortcuts import get_object_or_404
import questionnaire
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Questionnaire, Questions
from .serializers import (
    QuestionnaireListSerializer,
    QuestionnaireDetailSerializer,
    AnswerSerializer,
)


class QuestionnaireViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Questionnaire.objects.all()
        serializer = QuestionnaireListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Questionnaire.objects.all()
        questionnaire = get_object_or_404(queryset, pk=pk)
        serializer = QuestionnaireDetailSerializer(questionnaire)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Questions.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = AnswerSerializer(question)
        return Response(serializer.data)