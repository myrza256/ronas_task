import requests
import json

from django.conf.urls import url
from core.models import Weather
from weather_app.settings import API_KEY


def get_weather_and_save(name: str) -> Weather:

    url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'q': name, 'appid': API_KEY, 'units': 'metric'}  
    r = requests.get(url, params=payload)
    if r.status_code == 200:
        json_data = json.loads(r.text)
        main = json_data['main']
        weather_data = json_data['weather'][0]
        wind = json_data['wind']

        data = {
            "city": json_data['name'].lower(),
            "main": weather_data['main'],
            "description": weather_data['description'],
            "temp_c": main['temp'],
            "humidity": main['humidity'],
            "wind_speed": wind['speed'],
            "wind_deg": wind['deg']
        }
        weather = Weather(**data)
        weather.save()
        weather = Weather.objects.filter(city=data['city']).order_by('-updated_at')
    else:
        weather = {
            "status": r.status_code,
            "detail": "error on third party api"
        }

    return weather