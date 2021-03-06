from django.db.models import CharField, DateTimeField, IntegerField, ForeignKey
from django.db.models import Model, F
from django.db import models

from django.utils import timezone
import datetime as dt


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self) -> bool:
        time_elapsed = timezone.now() - self.pub_date
        return dt.timedelta() < time_elapsed <= dt.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(Model):
    question = ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def vote(self):
        self.votes = F('votes') + 1
        self.save()
