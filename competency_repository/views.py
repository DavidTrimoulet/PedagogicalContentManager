from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Welcome to the competency repository")


def get_skills(request):
    return HttpResponse("all skills")


def get_questions_for_skill(request, skill):
    return HttpResponse("Question for a skill")


def get_questions_for_a_prosit(request, prosit_number):
    return HttpResponse("Question for a skill")


def get_prosits(request):
    return HttpResponse("Question for a skill")


def generate_student_cctl(request):
    return HttpResponse("Question for a skill")


def generate_teacher_cctl(request):
    return HttpResponse("Question for a skill")


def add_question(request, question):
    return HttpResponse("Question for a skill")


def add_prosit(request, prosit):
    return HttpResponse("Question for a skill")