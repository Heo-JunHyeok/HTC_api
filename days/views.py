from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render
from .models import Training
from .serializers import TrainingSerializer

# Create your views here.


class TrainingList(ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
