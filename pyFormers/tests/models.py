from django.db import models


class Questions(models.Model):
    category = models.CharField(max_length=100)
    question_text = models.CharField(max_length=300)


class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
