from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.forms.models import formset_factory
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.timezone import now
from .models import Question, Test, RunTest, RunTestAnswers, NotedItem
from .forms import TestForm, QuestionForm, AnswerForm, NoteForm, Note
from .tasks import delete_test


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
    MINUTES = '20'
    DAYS = '30'

    context = {'name': new_object}
    if request.method == 'POST':
        if new_object == 'test':
            new_test = TestForm(request.POST)
            if new_test.is_valid():
                named_test = new_test.save(commit=False)
                if request.user.is_authenticated:
                    named_test.user = request.user.username
                else:
                    named_test.user = None
                named_test.save()

                if new_test.cleaned_data['delay'] == MINUTES:
                    minutes = int(new_test.cleaned_data['count'])
                    time_to_exp = now() + timedelta(minutes=minutes)
                    delete_test.apply_async((named_test.id,), eta=time_to_exp)

                elif new_test.cleaned_data['delay'] == DAYS:
                    days = int(new_test.cleaned_data['count'])
                    time_to_exp = now() + timedelta(days=days)
                    delete_test.apply_async((named_test.id,), eta=time_to_exp)


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
    if request.method == 'POST':
        test = get_object_or_404(Test, id=test_id)
        question = get_object_or_404(Question, id=q_id)

        test.questions.remove(question)
        return redirect(f'/tests/{test_id}?edit_test=edit')


def add_q(request, test_id, q_id):
    if request.method == 'POST':
        test = Test.objects.get(id=test_id)
        question = Question.objects.get(id=q_id)

        test.questions.add(question)
        return redirect(f'/tests/{test_id}?edit_test=edit')


def run_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    answer_factory = formset_factory(AnswerForm, min_num=len(questions))
    answer_form_set = answer_factory()

    if request.method == 'POST':
        answer_form_set = answer_factory(request.POST)
        if answer_form_set.is_valid():
            if request.user.is_authenticated:
                user_name = request.user.username
            else:
                user_name = None
            run_test_obj = RunTest(name=test.name, test=test, user=user_name)
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
    context = {'type_info': run_test_obj.name,
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
    test_obj = Test.objects.get(id=test_id)
    context = {'type_info': test_obj.name,
               'form': NoteForm,
               'notes_obj': NotedItem.objects.filter(content_type=ContentType.objects.get_for_model(test_obj),
                                                     object_id=test_id)}

    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = Note.objects.create(note=note_form.cleaned_data['note'])
            note_item = NotedItem(note=note,
                                  content_type=ContentType.objects.get_for_model(test_obj),
                                  object_id=test_id)
            note_item.save()

    return render(request, 'app_tests/notes.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def sign_up(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'app_tests/login_v.html', context=context)
    elif request.method == 'GET':
        form = UserCreationForm()
        context.update(form=form)
        return render(request, 'app_tests/signup_v.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'app_tests/login_v.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'app_tests/login_v.html', context=context)
