from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Question, Test, RunTest, RunTestAnswers, NotedItem

admin.site.register(Question)
admin.site.register(RunTest)
admin.site.register(Test)
admin.site.register(RunTestAnswers)
admin.site.register(NotedItem)

TokenAdmin.raw_id_fields = ('user',)