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

@csrf_exempt
def signUp(request):
    """This is the view funtion for user signup"""
    if request.method == 'POST':
        #email = request.POST.get('email')
        print(request)
        #return HttpResponse(email)
        
        data = JSONParser().parse(request)
        serializer = userSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
