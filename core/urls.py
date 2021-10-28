from django.urls import path

from core.views import WeatherAPIList


urlpatterns = [
    path('weather/', WeatherAPIList.as_view(), name='get-weather'),
]