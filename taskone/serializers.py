from rest_framework import serializers
from .models import NumberProperty
from .utils import check_properties, get_digit_sum, get_fun_fact #,generate_error_json_alphabet
import json

    
class NumberPropertySerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()  
    digit_sum = serializers.SerializerMethodField()   
    fun_fact = serializers.SerializerMethodField()   
    
    class Meta:
        model = NumberProperty
        fields = ["number", "is_prime", "is_perfect", "properties", "digit_sum", "fun_fact"]

    def get_properties(self, obj):
        return check_properties(obj.number) 

    def get_digit_sum(self, obj):
        return get_digit_sum(obj.number) 

    def get_fun_fact(self, obj):
        return get_fun_fact(obj.number) 
