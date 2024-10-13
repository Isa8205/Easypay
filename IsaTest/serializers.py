from .models  import Saccos, Vehicles, Destinations, Routes, Drivers, Conductors
from rest_framework import serializers

class SaccosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saccos
        fields = '__all__'

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = '__all__'

class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'

class ConductorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductors
        fields = '__all__'