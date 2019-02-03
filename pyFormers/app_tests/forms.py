from django import forms
from .models import Answers

AnswerForm = forms.modelformset_factory(Answers, fields='__all__', extra=0)
