from django.db import models

class User(models.Model):
    """This is the User model for database"""
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
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


