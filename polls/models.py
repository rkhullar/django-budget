from django.db.models import CharField, DateTimeField, IntegerField, ForeignKey
from django.db.models import Model
from django.db import models


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField('date published')


class Choice(Model):
    question = ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)
