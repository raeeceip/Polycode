from django.contrib import admin

from .models import Question, Choice

# crud.admin.py
admin.site.register(Question)
admin.site.register(Choice)
