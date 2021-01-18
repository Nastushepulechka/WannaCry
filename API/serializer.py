from rest_framework import serializers
from tasks.models import Tasks, Category, Status

class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'category', 'content', 'published', 'status']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'status']
