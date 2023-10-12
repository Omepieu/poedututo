from django.shortcuts import render

def list_matiere_quiz(request):
    return render(request, 'quiz/list_quiz.html')

def detail_matiere_quiz(request):
    return render(request, 'quiz/detail_quiz.html')

def question_quiz(request):
    return render(request, 'quiz/question_quiz.html')