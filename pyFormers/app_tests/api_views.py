from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Question, Test, RunTest, NotedItem
from . import serializers
from . import permissions


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (permissions.JWordUsersNotAllowed,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        model_object = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(model_object)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super(QuestionViewSet, self).create(request, *args, **kwargs)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = serializers.TestSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        model_object = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(model_object)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super(TestViewSet, self).create(request, *args, **kwargs)


class RunTestViewSet(viewsets.ModelViewSet):
    queryset = RunTest.objects.all()
    serializer_class = serializers.RunTestSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        model_object = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(model_object)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super(RunTestViewSet, self).create(request, *args, **kwargs)


class NotedItemViewSet(viewsets.ModelViewSet):
    queryset = NotedItem.objects.all()
    serializer_class = serializers.NoteItemSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
