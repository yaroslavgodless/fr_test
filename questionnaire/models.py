from django.db import models
from datetime import date
from django.urls import reverse
from django.db.models.deletion import CASCADE



class Questions(models.Model):
    user_id = models.CharField("ID пользователя", max_length=30, blank=True)
    text = models.CharField("Вопрос ", max_length=300, blank=True, null=True)
    answer = models.TextField("Ответ", max_length=300, blank=True, null=True)
    ANSWER_TYPE = [
    ('TXT', 'Текст'),
    ('UNO', 'Один вариант'),
    ('SOM', 'Несколько'),
    ]
    type = models.CharField("Тип вопроса", max_length=3, choices=ANSWER_TYPE, default='TXT')

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"



class Questionnaire(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.CharField("Описание", max_length=150)
    questions = models.ManyToManyField(Questions, related_name="questions")
    url = models.SlugField(max_length=160, unique=True)
    start_date = models.DateField("Дата старта опроса", default=date.today, editable=False)
    end_date = models.DateField("Дата окончания опроса")

    class Meta:
        verbose_name = "Опросник"
        verbose_name_plural = "Опросники"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("questionnaire_detail", kwargs={"slug": self.url})

    def get_questions(self):
        return self.questions_set.filter()

