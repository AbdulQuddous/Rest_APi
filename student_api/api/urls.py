from django.urls import path,include
from . import views
from .views import emoloyee
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employee',emoloyee , basename='employee' )
urlpatterns = [
    path('student',views.studentview),
    path('student/<int:pk>/',views.studentdetail),

    # path('employee',views.Employees.as_view()),
    # path('employee/<int:pk>/',views.Employedetail.as_view()),
    path('',include(router.urls))
]
