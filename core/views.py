from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, permissions

from core.models import Weather
from core.serializers import WeatherSerializer
from core.services import get_weather_and_save



class WeatherAPIList(generics.ListAPIView):
    serializer_class = WeatherSerializer
    #permission_classes = [permissions.IsAuthenticated, IsManagerUser]


    def get_queryset(self):
        try:
            name = self.request.GET['name']
        except ObjectDoesNotExist as e:
            raise "Provide the name of city"
            
        weather = Weather.objects.filter(city=name).order_by('-updated_at')
        if not weather:
            weather = get_weather_and_save(name)
        return weather