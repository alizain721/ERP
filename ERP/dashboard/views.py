from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer 
from rest_framework import status
from rest_framework.response import Response
from . import models
from .models import *
from .serializers import *
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

@csrf_exempt
@api_view(['POST',])
def user_projects(request):
    """This method or api function will return all projects of employee, given employee_id as parameter"""
    data = request.data
    user_id = data["user_id"]
    user_projects = UserProject.objects.filter(employee=user_id)
    user_projects_serializer = UserProjectSerializer(user_projects, many=True)
    return Response({"user_projects":user_projects_serializer.data},status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST',])
def employee_project_request (request):
    """This method or api function will create a user request to be added or removed from a particular project"""
    user_project_request_serializer = UserProjectRequestSerializer(data=request.data)
    if user_project_request_serializer.is_valid():
        user_project_request_serializer.save()
        return Response({"message":"Request added successfully"},status = status.HTTP_201_CREATED)
    else:
        return Response({"message":user_project_request_serializer.errors},status = status.HTTP_403_FORBIDDEN)
