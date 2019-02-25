from .models import Question, Test
from . import serialaizers
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serialaizers.QuestionSerialaizer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serialaizers.QuestionSerialaizer


class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = serialaizers.TestSerialaizer


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = serialaizers.TestSerialaizer
