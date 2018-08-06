from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signUp, name = 'signup'),
    path('user_projects',views.user_projects),
    path('employee_project_request',views.employee_project_request)
]
