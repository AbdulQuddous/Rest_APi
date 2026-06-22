from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def studentview(request):
    student={
        'name' : 'abdul',
        'age': '20'
    }
    return JsonResponse(student)