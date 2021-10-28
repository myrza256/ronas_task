from django.urls.conf import re_path

from core.views import WeatherAPIList


urlpatterns = [
    re_path('^weather/(?P<name>.+)/$', WeatherAPIList.as_view(), name='get-weather'),
]