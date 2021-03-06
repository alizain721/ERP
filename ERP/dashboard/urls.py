from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signUp, name = 'signup'),
    path('user_projects',views.user_projects),
    path('employee_project_request',views.employee_project_request),
    path('employee_requests_all',views.employee_requests_all),
    path('accept_request',views.accept_request),
    path('reject_request',views.reject_request),
    path('project_all_requests',views.project_all_requests)
]
