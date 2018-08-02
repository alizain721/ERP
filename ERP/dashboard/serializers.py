from rest_framework import serializers
from .models import User


class userSerializer(serializers.ModelSerializer):
    """This is the serializer class for serializing user model"""
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'profile_pic', 'contact_info')
