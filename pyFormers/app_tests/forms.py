from django import forms
from .models import Test, Question, Note


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note', ]
        widgets = {
            'note': forms.Textarea(attrs={'cols': 40,
                                          'rows': 8,
                                          'style': 'resize:none;'}),
            }


class AnswerForm(forms.Form):
    Answer = forms.CharField()
