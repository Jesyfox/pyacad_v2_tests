from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.forms.models import formset_factory
from django.contrib.contenttypes.models import ContentType
from .models import Question, Test, RunTest, RunTestAnswers, NotedItem
from .forms import TestForm, QuestionForm, AnswerForm, NoteForm, Note


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
    Question.objects.get(id=q_id).delete()

    return new_object(request, 'question')


def detail_of_test(request, test_id):
    context = {}
    if 'start_test' in request.GET:
        return run_test(request, test_id)
    elif 'edit_test' in request.GET:
        return edit_test(request, test_id)
    elif 'delete_test' in request.GET:
        get_object_or_404(Test, id=test_id).delete()
        return redirect('/')
    elif request.method == 'GET':
        tests = get_object_or_404(Test, id=test_id)
        questions = tests.questions.all()
        run_tests = RunTest.objects.filter(test=tests)
        context.update(test=tests, questions=questions, run_tests=run_tests)
        return render(request, 'app_tests/test_info.html', context=context)


def edit_test(request, test_id):
    context = {}
    if request.method == 'GET':
        test = get_object_or_404(Test, id=test_id)
        test_questions = test.questions.all()
        questions = Question.objects.all()

        context.update(test=test,
                       test_questions=test_questions,
                       questions=questions)
        return render(request, 'app_tests/edit_test.html', context=context)


def remove_q(request, test_id, q_id):
    test = get_object_or_404(Test, id=test_id)
    question = get_object_or_404(Question, id=q_id)

    test.questions.remove(question)
    return edit_test(request, test_id)


def add_q(request, test_id, q_id):
    test = Test.objects.get(id=test_id)
    question = Question.objects.get(id=q_id)

    test.questions.add(question)
    return edit_test(request, test_id)


def run_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    answer_factory = formset_factory(AnswerForm, min_num=len(questions))
    answer_form_set = answer_factory()

    if request.method == 'POST':
        answer_form_set = answer_factory(request.POST)
        if answer_form_set.is_valid():
            run_test_obj = RunTest(name=test.name, test=test)
            run_test_obj.save()
            for q, a in zip(questions, answer_form_set.cleaned_data):
                run_test_answer = RunTestAnswers(run_test=run_test_obj, question=str(q), answer=a['Answer'])
                run_test_answer.save()
            return redirect(f'/tests/{test_id}')

    context = {'formset': dict(zip(questions, answer_form_set)),
               'manage_form': answer_form_set,
               'test': test}
    return render(request, 'app_tests/start_quiz.html', context=context)


def run_test_detail(request, runtest_id):
    run_test_obj = get_list_or_404(RunTest, id=runtest_id)
    run_tests_answers = get_list_or_404(RunTestAnswers, run_test__in=run_test_obj)

    context = {'run_test': run_test_obj, 'run_tests_answers': run_tests_answers}

    return render(request, 'app_tests/run_test_detail.html', context=context)


def run_test_notes(request, runtest_id):
    run_test_obj = RunTest.objects.get(id=runtest_id)
    context = {'type_info': 'run_test',
               'form': NoteForm,
               'notes_obj': NotedItem.objects.filter(content_type=ContentType.objects.get_for_model(run_test_obj),
                                                    object_id=runtest_id)}

    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = Note.objects.create(note=note_form.cleaned_data['note'])
            note_item = NotedItem(note=note,
                                  content_type=ContentType.objects.get_for_model(run_test_obj),
                                  object_id=runtest_id)
            note_item.save()

    return render(request, 'app_tests/notes.html', context=context)


def test_notes(request, test_id):
    test_obj = RunTest.objects.get(id=test_id)
    context = {'type_info': 'test', 'form': NoteForm}

    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            pass

    return render(request, 'app_tests/notes.html', context=context)
