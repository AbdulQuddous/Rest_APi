from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student
# Create your views here.

def studentview(request):
    student=Student.objects.all()
    student_list = list(student.values())
    return JsonResponse(student_list , safe=False)