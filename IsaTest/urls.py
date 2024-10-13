from .views import SaccoView, SaccoDetailView
from django.urls import path
urlpatterns = [
    path('saccos/', SaccoView.as_view(), name='saccos' ),
    path('saccos/<int:pk>/', SaccoDetailView.as_view(), name='saccos_detail')
]