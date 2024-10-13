from .views import SaccoView, SaccoDetailView, VehiclesView, VehiclesDetailView, DestinationsView, DestinationsDetailView, RoutesView, RoutesDetailView, DriversView, DriversDetailView, ConductorsView, ConductorsDetailView
from django.urls import path
urlpatterns = [
    path('saccos/', SaccoView.as_view(), name='saccos' ),
    path('saccos/<int:pk>/', SaccoDetailView.as_view(), name='saccos_detail'),
    path('vehicles/', VehiclesView.as_view(), name='vehicles'),
    path('vehicles/<int:pk>/', VehiclesDetailView.as_view(), name='vehicles_detail'),
    path('destinations/', DestinationsView.as_view(), name='destinations'),
    path('destinations/<int:pk>/', DestinationsDetailView.as_view(), name='destinations_detail'),
    path('routes/', RoutesView.as_view(), name='routes'),
    path('routes/<int:pk>/', RoutesDetailView.as_view(), name='routes_detail'),
    path('drivers/', DriversView.as_view(), name='drivers'),
    path('drivers/<int:pk>/', DriversDetailView.as_view(), name='drivers_detail'),
    path('conductors/', ConductorsView.as_view(), name='conductors'),
    path('conductors/<int:pk>/', ConductorsDetailView.as_view(), name='conductors_detail'),
]