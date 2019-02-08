from django import forms
from .models import Test, Question


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', ]


class AnswerForm(forms.Form):
    Answer = forms.CharField()

