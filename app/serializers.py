from rest_framework import serializers
from .models import (Patient,Doctor,Consultation,RendezVous,Hotel,TravelAgency,MedicalCenter)


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ("id","userName","age","email","gender","jobTitle","bodyGroup","city","DiseaseDescription","phone","url")



class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id","userName","age","email","gender","jobTitle","city","addresse","phone","speciality","url")



class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id","hotelName","city","addresse","phone","photo","price","url")
