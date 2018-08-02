from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectSerializer
from .models import Project

class ProjectApiView(APIView):
    """Project APIview to handul all restfull requests"""
    def get(self,request, format=None):
        """This method will return either all projects or a signle proect"""
        project_id = request.GET.get('project_id')
        if project_id:
            project = Project.objects.filter(id=project_id)
            project_serializer = ProjectSerializer(project, many=True)
        else:
            projects = Project.objects.all()
            project_serializer = ProjectSerializer(projects, many=True)
        return Response({"data":project_serializer.data})

