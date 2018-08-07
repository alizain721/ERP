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

@csrf_exempt
@api_view(['POST',])
def employee_requests_all(request):
    """This method or api function will return all user_requets of employee, given employee_id as parameter"""
    data = request.data
    user_id = data["user_id"]
    user_requests = UserProjectRequest.objects.filter(employee=user_id)
    user_project_request_serializer = UserProjectRequestSerializer(user_requests, many=True)
    return Response({"user_requests":user_project_request_serializer.data},status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def accept_request(request):
    """ This method or api is for pm to accept request for employees to be added to project"""
    data = request.data
    request_id = data["request_id"]
    try:
        request = UserProjectRequest.objects.get(id=request_id)
        request.status = "accpted"
        request.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except UserProjectRequest.DoesNotExist:
        return Response({"message": "Record not found"},status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def reject_request(request):
    """ This method or api is for pm to reject request for employees to be added to project, it takes request_id and reason as input"""
    data = request.data
    request_id = data["request_id"]
    reason = data['reason']
    try:
        user_project_request = UserProjectRequest.objects.get(id=request_id)
        user_project_request.status = "rejected"
        user_project_request.reason = reason
        user_project_request.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except UserProjectRequest.DoesNotExist:
        return Response({"message": "Record not found"},status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def project_all_requests(request):
    """This api end point will return all pending requests for a project that are yet to be approved or rejected, taking project_id as input"""
    data = request.data
    project_id = data["project_id"]
    user_project_requests = UserProjectRequest.objects.filter(id=project_id,status='')
    user_project_request_serializer = UserProjectRequestSerializer(user_project_requests, many=True)
    if user_project_request_serializer.data:
        return Response({"Requests":user_project_request_serializer.data},status=status.HTTP_200_OK)
    return Response({"message": "Record not found"},status=status.HTTP_404_NOT_FOUND)
