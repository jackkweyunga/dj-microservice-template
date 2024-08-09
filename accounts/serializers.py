from rest_framework  import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','username', 'phone_number', 'full_name', 'profile_img']
        read_only_fields = ['id', 'email','username']
