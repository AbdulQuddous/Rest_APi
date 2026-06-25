from django.urls import path
from . import views

urlpatterns = [
    path('student',views.studentview),
    path('student/<int:pk>/',views.studentdetail),

    path('employee',views.Employees.as_view()),
    path('employee/<int:pk>/',views.Employedetail.as_view()),
]
