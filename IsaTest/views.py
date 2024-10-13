from django.shortcuts import render
from rest_framework import generics
from .serializers import SaccosSerializer, VehiclesSerializer, DestinationsSerializer, RoutesSerializer, DriversSerializer, ConductorsSerializer
from .models import Conductors, Destinations, Drivers, Routes, Saccos, Vehicles
# Create your views here.

def index(request):
    return render(request, 'index.html')

class SaccoView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = SaccosSerializer


class SaccoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = SaccosSerializer

class VehiclesView(generics.ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

class VehiclesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

class DestinationsView(generics.ListCreateAPIView):
    queryset = Destinations.objects.all().select_related()
    serializer_class = DestinationsSerializer

class DestinationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destinations.objects.all().select_related()
    serializer_class = DestinationsSerializer

class RoutesView(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class RoutesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class DriversView(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

class DriversDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

class ConductorsView(generics.ListCreateAPIView):
    queryset = Conductors.objects.all()
    serializer_class = ConductorsSerializer

class ConductorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conductors.objects.all()
    serializer_class = ConductorsSerializer

