from django import forms
from .models import Test, Question, Note


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', ]

    options = (
        ('10', 'None'),
        ('20', 'Minutes'),
        ('30', 'Days')
    )
    delay = forms.ChoiceField(label='Delay', widget=forms.Select, choices=options)
    count = forms.CharField(label='Count', widget=forms.NumberInput, required=False)


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
