from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer 
from rest_framework import status
from rest_framework.response import Response
from . import models
from .serializers import userSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
def signUp(request):
    """This is the view funtion for user signup and sigin with google authentication (frontend)"""
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = models.User.objects.get(email=data.get("email"))
        except models.User.DoesNotExist:
            user = None

        if user:
            if user.authenticate(data.get("email"), data.get("password")):
                user_serializer = userSerializer(user)
                return JsonResponse(user_serializer.data)
            else:
                return JsonResponse({"error": "incorrect Email or pasword"})

        else:
            serializer = userSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




