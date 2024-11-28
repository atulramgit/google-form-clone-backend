from django.urls import path, include
from quiz.views import QuestionAPI, FormAPI, StoreResponsesAPI, FormResponsesAPI

urlpatterns = [
    path('questions/', QuestionAPI.as_view()),
    path('form/<pk>/', FormAPI.as_view()),
    path('store-response/', StoreResponsesAPI.as_view()),
    path('form/responses/<pk>/', FormResponsesAPI.as_view()),
    
]
