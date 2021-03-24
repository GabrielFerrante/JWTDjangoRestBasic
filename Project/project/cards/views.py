from django.shortcuts import render
from django.core import exceptions
from .models import Card, Task
from .serializers import CardSerializer, TaskSerializer
from rest_framework import generics, permissions
from .utils import custom_permissions
from django.contrib.auth.models import User

class CardViewSet(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Card.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardViewSetD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsOwner
    ]


class TaskViewSet(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        card = Card.objects.filter(owner = self.request.user) 
        return Task.objects.filter(card__in = card)

    def perform_create(self, serializer):
        if serializer.validated_data['card'].owner != self.request.user:
            raise exceptions.PermissionDenied
        else:
            serializer.save()
   

class TaskViewSetD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [
        custom_permissions.IsCardOwner,
        permissions.IsAuthenticated,
        
    ]

