from django.contrib import admin

from .models import Questions, Answers, Categories

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Categories)
