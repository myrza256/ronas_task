from rest_framework import serializers

from core.models import City, Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'
