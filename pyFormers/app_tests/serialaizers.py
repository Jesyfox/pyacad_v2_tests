from rest_framework import serializers
from .models import Question, Test


class QuestionSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text')


class TestSerialaizer(serializers.ModelSerializer):
    questions = QuestionSerialaizer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'questions', 'user')
