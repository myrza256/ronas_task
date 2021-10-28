from django.shortcuts import render
from rest_framework import generics, permissions

from core.models import Weather
from core.serializers import WeatherSerializer
from core.services import get_weather_and_save



class WeatherAPIList(generics.ListAPIView):
    serializer_class = WeatherSerializer
    #permission_classes = [permissions.IsAuthenticated, IsManagerUser]


    def get_queryset(self):
        name = self.kwargs['name']
        weather = Weather.objects.filter(city__title=name)
        if not weather:
            weather = get_weather_and_save(name)
        return weather