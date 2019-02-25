from rest_framework import serializers
from .models import Question, Test, RunTest, RunTestAnswers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text')


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'questions', 'user')


class RunTestAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = RunTestAnswers
        fields = ('id', 'run_test', 'question', 'answer')


class RunTestSerializer(serializers.ModelSerializer):
    run_test_answers = RunTestAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = RunTest
        fields = ('id', 'name', 'test', 'run_test_answers', 'user')
