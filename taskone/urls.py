from django.urls import path
from .views import get_or_create_record, get_error

urlpatterns = [
    
    path("number-api/<int:number>/", get_or_create_record, name = "number-api-number"),
    path("number-api/<str:alphabet>/", get_error, name = "number-api-alphabet"),
]


