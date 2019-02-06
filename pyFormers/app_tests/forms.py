from django.forms.models import modelformset_factory, BaseModelFormSet
from django import forms
from .models import Test, Question, RunTestAnswers, RunTest


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', ]


AnswerFormSet = modelformset_factory(RunTestAnswers, exclude=['run_test'], formset=BaseModelFormSet, extra=0)
