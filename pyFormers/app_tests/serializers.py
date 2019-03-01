from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Test, RunTest, RunTestAnswers, NotedItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class AttachedNoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotedItem
        fields = ('id', 'note')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text')


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    user = UserSerializer()
    notes = AttachedNoteItemSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'name', 'questions', 'user', 'notes')


class RunTestAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTestAnswers
        fields = ('id', 'question', 'answer')


class RunTestSerializer(serializers.ModelSerializer):
    run_test_answers = RunTestAnswersSerializer(many=True,
                                                source='run_test')
    user = UserSerializer()
    notes = AttachedNoteItemSerializer(many=True)

    class Meta:
        model = RunTest
        fields = ('id', 'name', 'run_test_answers', 'user', 'notes')


class NoteTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name')


class NoteRunTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTest
        fields = ('id', 'name')


class NoteTargetField(serializers.Field):
    serializer_map = {Test: NoteTestSerializer,
                      RunTest: NoteRunTestSerializer}

    def to_representation(self, obj):
        return self.serializer_map[obj.__class__](obj).data


class NoteItemSerializer(serializers.ModelSerializer):
    target_field = NoteTargetField(source='content_object',
                                   read_only=True)

    class Meta:
        model = NotedItem
        fields = ('target_field', 'id', 'note')
