from rest_framework import serializers
from .models import CustomUser
import requests


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super(CustomUserSerializer, self).to_representation(instance)
        request = self.context.get('request', None)

        # if request:
        #     data['profile_pic'] = request.build_absolute_uri(instance.profile_pic.url) if instance.profile_pic else None
        return data