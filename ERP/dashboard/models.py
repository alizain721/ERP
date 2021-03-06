from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class User(User):
    """This is the User model for database"""
    profile_pic = models.CharField(blank=True, max_length=1000)
    contact_info = models.CharField(blank=True, max_length=30)

    def __str__(self):
        """This function is to get representation of User model"""
        return self.email

    def authenticate(self, email, password,):
        """This function is to authenticate user"""
        try:
            user = User.objects.get(email=email, password= password)
        except User.DoesNotExist:
            user = None
        if user:
            return True
        else:
            return False

class UserProject(models.Model):
    """This function is association class between user and projects"""
    status = models.CharField(max_length=30, blank=True)
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class UserProjectRequest(models.Model):
    """This is model class to handle requests of employees to be added to any project"""
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    request_type = models.CharField(max_length =50)
    status = models.CharField(max_length = 50, blank=True)
    reason = models.TextField(max_length = 100, blank=True)
    def save(self, *args, **kwargs):
        """ Function that converts request_type to lower case at the time of saving it in database"""
        self.request_type = self.request_type.lower()
        self.status = self.status.lower()
        return super(UserProjectRequest, self).save(*args, **kwargs)
