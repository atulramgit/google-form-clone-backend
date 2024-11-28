from django.db import models
from .choices import QUESTION_CHOICES
from django.contrib.auth.models import User
from .utils import generateRandomCode

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Choices(BaseModel):
    choice = models.CharField(max_length=100)
    
    def __str__(self):
        return self.choice
    

class Question(BaseModel):
    question = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100, choices=QUESTION_CHOICES)
    required = models.BooleanField(default=True)
    choices = models.ManyToManyField(Choices, related_name="question_choices", blank = True)
    
    def __str__(self):
        return self.question
    
    
class Form(BaseModel):
    code = models.CharField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=100, default="#3f363c")
    questions = models.ManyToManyField(Question, related_name="questions")
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = generateRandomCode(20).lower()
            
        super(Form, self).save(*args, **kwargs)
        

class ResponseAnswer(BaseModel):
    answer = models.CharField(max_length=100)
    answer_to = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "answer_to")
    
    def __str__(self):
        return self.answer
    
    
class Responses(BaseModel):
    code = models.CharField(max_length=100, unique=True, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="forms")
    responder_email = models.CharField(max_length=100, null = True, blank = True)
    responses = models.ManyToManyField(ResponseAnswer)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = generateRandomCode(20).lower()
            
        super(Responses, self).save(*args, **kwargs)
      