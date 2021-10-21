from django.db.models import fields
from rest_framework import serializers

from .models import Questionnaire, Questions



class QuestionnaireListSerializer(serializers.ModelSerializer):
    """Список опросов"""
    
    class Meta:
        model = Questionnaire
        fields = ("name", "description", "start_date")


class AnswerSerializer(serializers.ModelSerializer):
    """Прохождение опроса"""
    def create(self, validated_data):
        answer, _ = Questions.objects.update_or_create(
            user_id=validated_data.get('user_id', None),
            text=validated_data.get('text', None),
            defaults={'answer': validated_data.get("answer")}
        )
        return answer

    class Meta:
        model = Questions
        fields = ("text", "answer", "type")



class QuestionnaireDetailSerializer(serializers.ModelSerializer):
    """Раскрытый опросник"""
    questions = AnswerSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = ("name", "description", "questions")

