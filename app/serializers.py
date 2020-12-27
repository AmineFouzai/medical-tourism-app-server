from rest_framework import serializers
from .models import (Patient,Doctor,Consultation,RendezVous,Hotel,TravelAgency,MedicalCenter)


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
