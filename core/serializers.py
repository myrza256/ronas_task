from rest_framework import serializers

from core.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = (
            'id',
            'created_at',
            'updated_at',
            'city',
            'main',
            'temp_c',
            'temp_f',
            'humidity',
            'wind_speed',
            'wind_deg'
        )
