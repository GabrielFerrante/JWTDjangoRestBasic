from rest_framework import serializers
from .models import Card, Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Task
        fields = ['id','description','done','card', ]


class CardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True,read_only=True)
    class Meta:
        model = Card
        fields = ['id','title', 'description', 'status', 'tasks', 'owner']





