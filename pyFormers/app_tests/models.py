from django.db import models
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.text}'


class Test(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f'{self.name}'


class RunTest(models.Model):
    name = models.CharField(max_length=100)
    questions = ArrayField(models.CharField(max_length=200))
    answers = ArrayField(models.CharField(max_length=200))
