from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from student.models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def studentview(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
