from django.contrib.auth.models import User
from django.http import JsonResponse
from pydantic import Json
from rest_framework.decorators import api_view


@api_view(['POST'])
def register_user(request):
    return JsonResponse({'message':'User created successfully', 'success':True})


@api_view(['POST'])
def authenticate_user(request):
    return JsonResponse({'message':'user authenticated', 'success':True})
