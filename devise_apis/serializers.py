from rest_framework import serializers
from agriapp.models import DeviseApis
from rest_framework.decorators import api_view

class DeviseApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviseApis
        fields = '__all__'
        