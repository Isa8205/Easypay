from django.shortcuts import render
from rest_framework import generics
from .serializers import SaccosSerializer
from .models import Saccos
# Create your views here.

class SaccoView(generics.ListCreateAPIView):
    queryset = Saccos.objects.all()
    serializer_class = SaccosSerializer


class SaccoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saccos.objects.all()
    serializer_class = SaccosSerializer