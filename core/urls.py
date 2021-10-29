from django.urls.conf import re_path

from core.views import WeatherAPIList


urlpatterns = [
    re_path('^weather/', WeatherAPIList.as_view(), name='get-weather'),
]