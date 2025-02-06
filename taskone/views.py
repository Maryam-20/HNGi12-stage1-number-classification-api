from urllib import request
import requests
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import json

from .serializers import NumberPropertySerializer
from .models import NumberProperty
from .utils import check_is_prime, check_is_perfect, generate_error_json_alphabet, is_valid_float


# Create your views here.


@api_view(['GET'])
def classify_number(request):
    number = request.query_params.get('number', None)

    if number is None:
        return Response({"error": "Missing number parameter"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        
        number = number.strip()
        if not number or number == '-' or (number[0] == '-' and not number[1:].isdigit()) or (number[0] != '-' and not number.isdigit()):
            return Response(json.loads(generate_error_json_alphabet(number)), status=status.HTTP_400_BAD_REQUEST)
        
        if is_valid_float(number) and not number.lstrip('-').isdigit():
            return Response(json.loads(generate_error_json_alphabet(number)), status=status.HTTP_400_BAD_REQUEST)
        
        number = int(number)  
        record, created = NumberProperty.objects.get_or_create(number=number)
        
        record.is_prime = check_is_prime(number)
        record.is_perfect = check_is_perfect(number)
        record.save()

        serializer = NumberPropertySerializer(record)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        