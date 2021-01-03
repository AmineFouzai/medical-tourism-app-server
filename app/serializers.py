from rest_framework import serializers

from .models import (Patient,Doctor,Consultation,RendezVous,Hotel,TravelAgency,MedicalCenter)


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ("id","firstname","lastname","age","email","password","gender","address","phone","url")



class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id","firstname","lastname","email","password","address","phone","speciality","price","url")



class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id","name","address","email","password","phone","photo","price","url")
    
