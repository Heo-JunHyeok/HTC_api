from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from .models import Health, Count
from .serializers import HealthSerializer, CountSerializer

# Create your views here.


class HealthList(ListCreateAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class HealthDetail(RetrieveUpdateDestroyAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class DailyHealth(ListCreateAPIView):
    queryset = Count.objects.all()
    serializer_class = CountSerializer
