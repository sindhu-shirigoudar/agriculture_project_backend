from django.shortcuts import render
from .serializers import DeviseApiSerializer
from agriapp.models import DeviseApis, Devise
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def get_api_list(request):
    all_apis = DeviseApis.objects.all()
    serializer = DeviseApiSerializer(all_apis, many=True)
    return JsonResponse({'data':serializer.data})

@api_view(['POST'])
def get_devise_by_devise_id(request):
    try:
        devise_id = request.POST['devise_id']
        devise = Devise.objects.filter(devise_id=devise_id).first()
        if devise:
            return Response({'device' : devise.pk}, status.HTTP_200_OK)
        else:
            return Response({'message' : 'Please send valid devse id'}, status.HTTP_400_BAD_REQUEST)
    except  Exception as e:
        return Response({'message' : "Something went wrong whilr fetching data please check the data"}, status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def add_location(request):
#     serializer = DeviseApiSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CRETED)

@api_view(['POST'])
def add_soil_data(request):
    serializer = DeviseApiSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message' : 'Soil data added successfully'}, status=status.HTTP_200_OK)
        
