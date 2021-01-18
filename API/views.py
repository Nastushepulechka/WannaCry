from django.http import JsonResponse
from rest_framework import viewsets
from tasks.models import Tasks, Category, Status
from .serializer import TasksSerializer, CategorySerializer, StatusSerializer

class TasksViewset(viewsets.ModelViewSet):
    serializer_class = TasksSerializer

    def get_queryset(self):
        ttasks = Tasks.objects.all()
        return ttasks

class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category

class StatusViewset(viewsets.ModelViewSet):
    serializer_class = StatusSerializer

    def get_queryset(self):
        status = Status.objects.all()
        return status

