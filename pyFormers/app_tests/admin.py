from django.contrib import admin

from .models import Question, Test, RunTest, RunTestAnswers

admin.site.register(Question)
admin.site.register(RunTest)
admin.site.register(Test)
admin.site.register(RunTestAnswers)