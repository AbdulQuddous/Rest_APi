from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from student.models import Student
from .serializers import StudentSerializer

@api_view(['GET' , 'POST'])
def studentview(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET' , 'DELETE' , 'PUT'])
def studentdetail(request , pk):
    try:
        student = Student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


