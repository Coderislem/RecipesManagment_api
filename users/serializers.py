from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSzeializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']



class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    
    
