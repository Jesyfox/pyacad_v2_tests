from django.shortcuts import render, redirect
from .models import Question, Test
from .forms import TestForm, QuestionForm


def index(request):
    tests = None
    questions = None
    context = {}
    if 'search' in request.GET:
        tests = Test.objects.filter(name__icontains=request.GET['title'])
    elif request.method == 'GET':
        tests = Test.objects.all()
        questions = Question.objects.all()
    context.update(tests=tests, questions=questions)
    return render(request, 'app_tests/index.html', context=context)


def new_object(request, new_object):
    context = {'name': new_object}
    if request.method == 'POST':
        if new_object == 'test':
            new_test = TestForm(request.POST)
            if new_test.is_valid():
                new_test.save()

        elif new_object == 'question':
            new_question = QuestionForm(request.POST)
            if new_question.is_valid():
                new_question.save()
            return redirect('/new_question')

        return redirect('/')

    elif request.method == 'GET':
        if new_object == 'test':
            context.update(form=TestForm)
        elif new_object == 'question':
            questions = Question.objects.all()
            context.update(form=QuestionForm, questions=questions)

        return render(request, 'app_tests/new_object.html', context=context)


def delete_question(request, q_id):
    Question.objects.filter(id=q_id).delete()
    return new_object(request, 'question')


def detail_of_test(request, test_id):
    if 'start_test' in request.GET:
        return run_test(request, test_id)
    elif 'delete_test' in request.GET:
        Test.objects.filter(id=test_id).delete()
        return redirect('/')
    elif request.method == 'GET':
        tests = Test.objects.get(id=test_id)
        context = {'test': tests}
        return render(request, 'app_tests/test_info.html', context=context)


def run_test(request, category_id):
    if request.method == 'POST':
        print('\n' * 10, request.POST)
    elif request.method == 'GET':
        form = None
        context = {'form': form}
        return render(request, 'app_tests/start_quiz.html', context=context)
