from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username','first_name', 'last_name',  'api_token', 'password']
        extra_kwargs = {'password': {'write_only': True}}
