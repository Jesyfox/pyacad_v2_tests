from .models import Question
from .serialaizers import QuestionSerialaizer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class QuestionList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serialaizer = QuestionSerialaizer(questions, many=True)
        return Response(serialaizer.data)

    def post(self, request, format=None):
        serialaizer = QuestionSerialaizer(data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)
        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serialaizer = QuestionSerialaizer(question)
        return Response(serialaizer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serialaizer = QuestionSerialaizer(question, data=request.data)
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data)
        return Response(serialaizer.errors)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
