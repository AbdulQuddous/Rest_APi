from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, studentview, studentdetail, blog , comment

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('student/', studentview),
    path('student/<int:pk>/', studentdetail),
    path('', include(router.urls)),
    path('blog/', blog.as_view()),
    path('comment/', comment.as_view()),
]
