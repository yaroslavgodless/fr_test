from django.contrib import admin
from .models import Questionnaire, Questions


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "start_date")
    list_display_links = ("name", "description")

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("text", "answer")
    list_display_links = ("text", "answer")