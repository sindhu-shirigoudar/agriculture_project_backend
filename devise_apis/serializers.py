from rest_framework import serializers
from agriapp.models import DeviseApis, DeviseLocation
from rest_framework.decorators import api_view

class DeviseApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviseApis
        fields = '__all__'

# class DeviseLocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeviseLocation
#         fields = (
#             'devise',
#             'latitude',
#             'longitude',
#         )
        