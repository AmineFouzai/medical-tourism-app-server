from django.shortcuts import render
from .models import (Patient, Doctor, Consultation,
                     RendezVous, Hotel, TravelAgency, MedicalCenter)
from .serializers import (PatientSerializer, DoctorSerializer, HotelSerializer)
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.http.response import JsonResponse
from django.core import serializers
# from rest_framework.parsers import FileUploadParser,FormParser,MultiPartParser

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctortViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # parser_classes = [FileUploadParser,MultiPartParser,FormParser]


@csrf_exempt
def login(request):
    import json
    if request.method == "POST":
        data = json.loads(request.body)
        if data['type'] == "patient":
            try:
                user =  Patient.objects.get(
                    email=data['email'], password=data['password']) 
            except Exception as e :
                user= None 
            return JsonResponse(serializers.serialize('python', [user]),safe=False) if user else HttpResponseBadRequest(JsonResponse({
                "message": "user not found"
            }))
        elif data['type'] == "hotel":
            try:
                user = Hotel.objects.get(
                    email=data['email'], password=data['password']) 
            except Exception as e :
                user= None 
            return JsonResponse(serializers.serialize('python', [user]),safe=False) if user else HttpResponseBadRequest(JsonResponse({
                "message": "user not found"
            }))
        else:
            try:
                user = Doctor.objects.get(
                    email=data['email'], password=data['password']) 
            except Exception as e :
                user= None 
            return JsonResponse(serializers.serialize('python', [user]),safe=False) if user  else  HttpResponseBadRequest(JsonResponse({
                "message": "user not found"
            }))