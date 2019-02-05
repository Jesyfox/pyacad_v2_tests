from django.shortcuts import render, redirect
from .models import Question, Test
from .forms import TestForm


def index(request):
    tests = None
    context = {}
    if 'search' in request.GET:
        tests = Test.objects.filter(name__icontains=request.GET['search'])
    elif request.method == 'GET':
        tests = Test.objects.all()
    context.update(tests=tests)
    return render(request, 'app_tests/index.html', context=context)


def new_object(request, new_object):
    context = {'name': new_object}
    if request.method == 'POST':
        if new_object == 'test':
            new_test = TestForm(request.POST)
            if new_test.is_valid():
                new_test.save()
        elif new_object == 'question':
            context.update(form='its question')
        redirect('index')
    elif request.method == 'GET':
        if new_object == 'test':
            context.update(form=TestForm)
        elif new_object == 'question':
            context.update(form='its question')
        return render(request, 'app_tests/new_object.html', context=context)


def detail_of_test(request, test_id):
    if 'start_test' in request.GET:
        return run_test(request, test_id)
    elif request.method == 'GET':
        tests = Test.objects.filter(id=test_id)[0]
        context = {'tests': tests}
        return render(request, 'app_tests/test_info.html', context=context)


def run_test(request, category_id):
    if request.method == 'POST':
        print('\n' * 10, request.POST)
    elif request.method == 'GET':
        form = None
        context = {'form': form}
        return render(request, 'app_tests/start_quiz.html', context=context)
