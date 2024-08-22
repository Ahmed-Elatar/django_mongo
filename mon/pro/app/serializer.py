from rest_framework import serializers
from .models import *



class Try_2Serializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=100)

    def create(self, data):
        return Try_2.objects.create(**data)
        
    