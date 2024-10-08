from django.urls import path

from authentication import views

urlpatterns = [
    path('register/', views.signup, name='register')
]