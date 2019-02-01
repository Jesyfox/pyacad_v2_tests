from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Questions(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.category}: {self.question_text}'


class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
