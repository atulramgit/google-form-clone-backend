from rest_framework import serializers
from .models import Question, Form, ResponseAnswer, Responses

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["created_at", "updated_at"]
        
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ["created_at", "updated_at", "creator", "id"]
        
    def to_representation(self, instance):
        questions = []
        for question in instance.questions.all():
            choices = None
            if question.question_type in ["multiple choice", "checkbox"]:
                choices = []
                for choice in question.choices.all():
                    choices.append({"id" : choice.id, "choice" : choice.choice})
                    
            questions.append({
                "id" : question.id,
                "question" : question.question,
                "question_type" : question.question_type,
                "required" : question.required,
                "choices" : choices,
            })
            
        data = {
            "code" : instance.code,
            "title" : instance.title,
            "background_color" : instance.background_color,
            "questions" : questions,
        }
        
        return data
    
    
class ResponseAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseAnswer
        fields = '__all__'
        
    def to_representation(self, instance):
        data = {
            "answer" : instance.answer,
            "answer_to" : {
                "question" : instance.answer_to.question,
                "question_type" : instance.answer_to.question
            }
        }
        
        return data
    
class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model : Responses
        exclude = ["created_at", "updated_at"]
        
    def to_representation(self, instance):
        data = {
            "id" : instance.id,
            "code" : instance.code,
            "responder_email" : instance.responder_email,
            "answers" : ResponseAnswerSerializer(instance.responses.all(), many = True).data
        }
        
        return data
    
class FormResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ["created_at", "updated_at", "creator", "id"]
        
    def to_representation(self, instance):
        query_set = Responses.objects.filter(form = instance)
            
        data = {
            "code" : instance.code,
            "title" : instance.title,
            "background_color" : instance.background_color,
            "responses" : ResponsesSerializer(query_set, many=True).data,
        }
            
        return data