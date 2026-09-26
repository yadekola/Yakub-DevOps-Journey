from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


students = [
    {
        "id": 1,
        "name": "John Doe",
        "course": "DevOps Engineering"
    },
    {
        "id": 2,
        "name": "Sarah James",
        "course": "Data Engineering"
    }
]


@api_view(["GET"])
def home(request):
    return Response({
        "message": "Welcome to the Student API"
    })


@api_view(["GET"])
def health(request):
    return Response({
        "status": "healthy"
    })


@api_view(["GET", "POST"])
def student_list(request):

    if request.method == "GET":
        return Response(students)

    if request.method == "POST":

        student = {
            "id": len(students) + 1,
            "name": request.data.get("name"),
            "course": request.data.get("course")
        }

        students.append(student)

        return Response(student, status=201)