from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("health/", views.health),
    path("students/", views.student_list),
]