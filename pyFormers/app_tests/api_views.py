from .models import Question, Test, RunTest, NotedItem
from . import serialaizers
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serialaizers.QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serialaizers.QuestionSerializer


class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = serialaizers.TestSerializer


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = serialaizers.TestSerializer


class RunTestList(generics.ListCreateAPIView):
    queryset = RunTest.objects.all()
    serializer_class = serialaizers.RunTestSerializer


class RunTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RunTest.objects.all()
    serializer_class = serialaizers.RunTestSerializer


class NotedItemList(generics.ListCreateAPIView):
    queryset = NotedItem.objects.all()
    serializer_class = serialaizers.NoteItemSerializer
