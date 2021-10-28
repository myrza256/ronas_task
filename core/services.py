import requests

from django.conf import settings
from django.conf.urls import url
from core.models import Weather


def get_weather_and_save(name: str) -> Weather:
    url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'q': name, 'appid': settings.API_KEY}  
    r = requests.get(url, params=payload)
    pass