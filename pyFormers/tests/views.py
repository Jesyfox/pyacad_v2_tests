from django.shortcuts import render
from django import forms
from .models import Questions, Categories


class CommentForm(forms.Form):
    answer = forms.CharField()


def index(request):
    if request.method == 'GET':
        categories_cont = Categories.objects.all()
        context = {'categories': categories_cont}
        return render(request, 'tests/index.html', context=context)


def category_detail(request, category_id):
    if 'start' in request.GET:
        return run_test(request, category_id)
    elif request.method == 'GET':
        category = Categories.objects.filter(id=category_id)[0]
        context = {'category': category}
        return render(request, 'tests/category_info.html', context=context)


def run_test(request, category_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print('\n'*10, form.cleaned_data)
    elif request.method == 'GET':
        category_questions = Questions.objects.filter(category=category_id)
        context = {'questions': category_questions, 'form': CommentForm}
        return render(request, 'tests/start_quiz.html', context=context)
