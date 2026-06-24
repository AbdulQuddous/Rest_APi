from django.urls import path
from . import views

urlpatterns = [
    path('student',views.studentview),
    path('student/<int:pk>/',views.studentdetail)
]
