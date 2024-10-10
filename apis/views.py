import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authentication.models import Users
from .models import Somebody

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    print(users)

    return render(request, 'users.html', {'users': users})

@api_view(['POST'])
def post_somebody(request):
    user = Somebody()
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    user.firstname = data.get('firstname')
    user.lastname = data.get('lastname')
    user.age = 18
    user.phone = data.get('phone')
    print(data)
    user.save()

    return Response({'status': 'success'})
