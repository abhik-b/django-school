from django.db import models
from classs.models import Classs
# Create your models here.


class Assignment(models.Model):
    marks = models.IntegerField(default=0)
    subject = models.CharField(max_length=120)
    class_name = models.ForeignKey(
        Classs, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "Subject- {}  Assignment # {}".format(self.subject, self.id)


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=500)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "Choice #{} for question {} -  {}".format(self.id, self.question.question_text, self.choice_text)
