from django.shortcuts import render
from .models import (Patient, Doctor, Consultation,
                     RendezVous, Hotel, TravelAgency, MedicalCenter)
from .serializers import (PatientSerializer, DoctorSerializer, HotelSerializer)
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core import serializers


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctortViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


class HotelViewSet(viewsets.ModelViewSet):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def login(request):
    import json
    if request.method == "POST":
        data = json.loads(request.body)
        if data['userType'] == "patient":

            try:
                user =  Patient.objects.get(
                    email=data['email'], password=data['password']) 
            except Exception as e :
                user= None 
            return JsonResponse(serializers.serialize('python', [user]),safe=False) if user else JsonResponse({
                "error": "user not found"
            })

        else:
            try:
                user =  Doctor.objects.get(
                    email=data['email'], password=data['password']) 
            except Exception as e :
                user= None 
            return JsonResponse(serializers.serialize('python', [user]),safe=False) if user  else  JsonResponse({
                "error": "user not found"
            })
