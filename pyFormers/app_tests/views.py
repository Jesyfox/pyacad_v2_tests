from django.shortcuts import render
from .models import Questions, Categories
from .forms import AnswerForm


def index(request):
    if 'search' in request.GET:
        categories_cont = Categories.objects.filter(name__icontains=request.GET['title'])
    elif request.method == 'GET':
        categories_cont = Categories.objects.all()
    context = {'categories': categories_cont}
    return render(request, 'app_tests/index.html', context=context)


def category_detail(request, category_id):
    if 'start_test' in request.GET:
        return run_test(request, category_id)
    elif request.method == 'GET':
        category = Categories.objects.filter(id=category_id)[0]
        context = {'category': category}
        return render(request, 'app_tests/category_info.html', context=context)


def run_test(request, category_id):
    if request.method == 'POST':
        print('\n' * 10, request.POST)
    elif request.method == 'GET':
        form = AnswerForm(queryset=Questions.objects.filter(category=category_id))
        context = {'form': form}
        return render(request, 'app_tests/start_quiz.html', context=context)
