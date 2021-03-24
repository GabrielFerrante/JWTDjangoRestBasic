from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
   CardViewSet,
   CardViewSetD,
   TaskViewSet,
   TaskViewSetD

)


urlpatterns = [
   path('cards/',CardViewSet.as_view(),name='cards'),
   path('cards/<int:pk>/', CardViewSetD.as_view(), name='card'),
   path('tasks/', TaskViewSet.as_view(),name='tasks'),
   path('tasks/<int:pk>/', TaskViewSetD.as_view(), name='task')
]