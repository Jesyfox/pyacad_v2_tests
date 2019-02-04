from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Question, Test


def index(request):
    tests = None
    context = {}
    if 'search' in request.GET:
        tests = Test.objects.filter(name__icontains=request.GET['title'])
    elif request.method == 'GET':
        tests = Test.objects.all()
    context.update(tests=tests)
    return render(request, 'app_tests/index.html', context=context)


def test_detail(request, category_id):
    if 'start_test' in request.GET:
        return run_test(request, category_id)
    elif request.method == 'GET':
        category = Test.objects.filter(id=category_id)[0]
        context = {'category': category}
        return render(request, 'app_tests/category_info.html', context=context)


def run_test(request, category_id):
    if request.method == 'POST':
        print('\n' * 10, request.POST)
    elif request.method == 'GET':
        form = None
        context = {'form': form}
        return render(request, 'app_tests/start_quiz.html', context=context)
