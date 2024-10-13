from django.shortcuts import render
from rest_framework import generics
from .serializers import SaccosSerializer, VehiclesSerializer, DestinationsSerializer, RoutesSerializer, DriversSerializer, ConductorsSerializer
from .models import Saccos
# Create your views here.

class SaccoView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = SaccosSerializer


class SaccoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = SaccosSerializer

class VehiclesView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = VehiclesSerializer

class VehiclesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = VehiclesSerializer

class DestinationsView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = DestinationsSerializer

class DestinationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = DestinationsSerializer

class RoutesView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = RoutesSerializer

class RoutesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = RoutesSerializer

class DriversView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = DriversSerializer

class DriversDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = DriversSerializer

class ConductorsView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = ConductorsSerializer

class ConductorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = ConductorsSerializer

