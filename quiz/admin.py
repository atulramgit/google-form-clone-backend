from django.contrib import admin
from .models import Choices, Question, Form, ResponseAnswer, Responses

# Register your models here.

admin.site.register(Choices)
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(ResponseAnswer)
admin.site.register(Responses)
