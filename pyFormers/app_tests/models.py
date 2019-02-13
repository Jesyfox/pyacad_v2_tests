from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

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
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class RunTestAnswers(models.Model):
    run_test = models.ForeignKey(RunTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)

    def __str__(self):
        return f'run_test "{self.run_test}", question: {self.question}, answer: {self.answer}'


class Note(models.Model):
    name = models.CharField(max_length=100)


class NotedItem(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
