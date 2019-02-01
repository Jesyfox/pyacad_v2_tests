from django.shortcuts import render
from .models import Questions, Categories


def index(request):
    if request.method == 'GET':
        categories_cont = Categories.objects.all()
        context = {'categories': categories_cont}
        return render(request, 'tests/index.html', context=context)


def category_detail(request, category_id):
    if request.method == 'GET':
        category = Categories.objects.filter(id=category_id)[0]
        context = {'category': category}
        print(category)
        return render(request, 'tests/category_info.html', context=context)
