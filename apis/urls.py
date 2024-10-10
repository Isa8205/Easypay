from django.urls import path

from apis import views

urlpatterns = [
    path('get-users/', views.get_users, name='get_users'),
    path('add-some', views.post_somebody, name='add')
]