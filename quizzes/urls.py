from django.urls import path
from quizzes.views import list_matiere_quiz, detail_matiere_quiz, question_quiz
APP_NAME = 'quizzes'
urlpatterns = [
    path('', list_matiere_quiz, name="list_quiz"),
    path('detail/', detail_matiere_quiz, name="detail_quiz"),
    path('question/', question_quiz, name="question_quiz"),
]
