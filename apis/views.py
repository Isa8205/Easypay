from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authentication.models import Users

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    print(users)

    return render(request, 'users.html', {'users': users})
