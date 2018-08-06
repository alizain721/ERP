from rest_framework import serializers
from .models import User,UserProject


class userSerializer(serializers.ModelSerializer):
    """This is the serializer class for serializing user model"""
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'profile_pic', 'contact_info')

class UserProjectSerializer(serializers.ModelSerializer):
    """This is the serializer class for UserProject"""
    class Meta:
        """Meta class for UserProject"""
        model = UserProject
        fields = ('status', 'employee','project')
