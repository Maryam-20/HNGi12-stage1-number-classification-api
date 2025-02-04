from urllib import request
import requests
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import json

from .serializers import NumberPropertySerializer
from .models import NumberProperty
from .utils import check_is_prime, check_is_perfect


# Create your views here.


@api_view(['GET'])
def get_or_create_record(request, number):
    try:
        record, created = NumberProperty.objects.get_or_create(number=number)
        print(record)
        
        if not created:
            record.is_prime = check_is_prime(number)
            record.is_perfect  = check_is_perfect(number)
            record.save()
        
        serializer = NumberPropertySerializer(record)
        return Response(serializer.data, status= status.HTTP_200_OK)
            
    except Exception as e:
        return Response( {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])        
def get_error(request, alphabet):
    error_dict = {"number": "alphabet", "error": True}
    return Response(error_dict, status=status.HTTP_400_BAD_REQUEST)
        