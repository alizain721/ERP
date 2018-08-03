from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer
from .models import Project

class ProjectApiView(APIView):
    """Project APIview to handul all restfull requests"""
    def get(self,request, format=None):
        """This method will return either all projects or a signle proect"""
        project_id = request.GET.get('project_id')
        if project_id:
            project = Project.objects.filter(id=project_id)
            if project:
                project_serializer = ProjectSerializer(project, many=True)
            else:
                return Response({"message":"No record found"},status = status.HTTP_404_NOT_FOUND)
        else:
            projects = Project.objects.all()
            project_serializer = ProjectSerializer(projects, many=True)
        return Response({"data":project_serializer.data})

    def post(self,request, format=None):
      """This method will crete a new project object """
      project_serializer = ProjectSerializer(data=request.data)
      if project_serializer.is_valid():
        project_serializer.save()
        return Response({"message":"Project created successfully"},status = status.HTTP_201_CREATED)
      else:
          return Response({"message":project_serializer.errors},status = status.HTTP_403_FORBIDDEN)

    def put(self,request,format=None):
        """This method will be used to update project"""
        project_id = request.data["id"]
        project = Project.objects.filter(id=project_id)
        if project:
            project_serializer = ProjectSerializer(project, data=request.data)
            if project_serializer.is_valid():
                project_serializer.save()
                return Response(project_serializer.data)
            else:
                return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message : Bad Request"},status=status.HTTP_400_BAD_REQUEST)
