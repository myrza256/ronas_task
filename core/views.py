from django.shortcuts import render
from rest_framework import generics, permissions

from core.models import Weather
from core.serializers import WeatherSerializer

class WeatherAPIList(generics.ListAPIView):
    serializer_class = WeatherSerializer
    #permission_classes = [permissions.IsAuthenticated, IsManagerUser]
    queryset = Weather.objects.all()


    #def get