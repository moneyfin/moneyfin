from rest_framework.serializers import ModelSerializer, Serializer
from apps.user.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
