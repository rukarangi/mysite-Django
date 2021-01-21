from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello worlds! Welcome to polls index.")

def detial(request, question_id):
    return HttpResponse("You're looking at question%s." % question.id)

def results(request, question_id):
    response = "You're looking at the resulst of question %s."
    return 



# Create your views here.
