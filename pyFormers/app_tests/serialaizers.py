from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Test, RunTest, RunTestAnswers, NotedItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', )


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Test
        fields = ('id', 'name', 'questions', 'user')


class RunTestAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTestAnswers
        fields = ('question', 'answer')


class RunTestSerializer(serializers.ModelSerializer):
    run_test_answers = RunTestAnswersSerializer(many=True,
                                                source='run_test')
    user = UserSerializer()

    class Meta:
        model = RunTest
        fields = ('id', 'name', 'run_test_answers', 'user')


class NoteTargetField(serializers.Field):
    serializer_map = {Test: TestSerializer,
                      RunTest: RunTestSerializer}

    def to_representation(self, obj):
        return self.serializer_map[obj.__class__](obj).data


class NoteItemSerializer(serializers.ModelSerializer):
    target_obj = NoteTargetField(source='content_object',
                                 read_only=True,)

    class Meta:
        model = NotedItem
        fields = ('target_obj', 'note')
