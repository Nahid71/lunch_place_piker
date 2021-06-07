'''
Serialize all data here.
'''
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    '''
    Serialize CustomUser model
    '''
    class Meta:
        model = CustomUser
        fields = '__all__'
    def to_representation(self, instance):
        data = super(CustomUserSerializer, self).to_representation(instance)
        request = self.context.get('request', None)
        return data


class UserLoginSerializer(serializers.Serializer):
    '''
    serializer login date here
    '''
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class UserLogoutSerializer(serializers.Serializer):
    '''
    serializer logout date here
    '''
    email = serializers.EmailField(required=False)
