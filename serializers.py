from rest_framework import serializers
from .models import (Patient,Doctor,Consultation,RendezVous,Hotel,TravelAgency,MedicalCenter,Reservation)

class RendezVousSerializer(serializers.ModelSerializer):
    consultation = ConsultationSerializer(many=True, read_only=True)
    doctor = DoctorSerializer(many=True, read_only=True)
    patient = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = RendezVous
        fields = ("id", "doctor", "patient", "Symptoms", "date", "consultation", "url")

class PatientSerializer(serializers.ModelSerializer):
    rendezvous = RendezVousSerializer(many=True, read_only=True)
    consultations = ConsultationSerializer(many=True, read_only=True)
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ("id","firstname","lastname","age","email","password","gender","address","phone","url","rendezvous","consultations","reservations")

class DoctorSerializer(serializers.ModelSerializer):
    rendezvous = RendezVousSerializer(many=True, read_only=True)
    consultations = ConsultationSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ("id","firstname","lastname","email","password","address","phone","speciality","price","url","rendezvous","consultations")

class HotelSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Hotel
        fields = ("id","name","address","email","password","phone","photo","price","url","reservations")

class ConsultationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=True, read_only=True)
    patient = PatientSerializer(many=True, read_only=True)
    rendezVous = RendezVousSerializer(many=True, read_only=True)

    class Meta:
        model = Consultation
        fields = ("id", "rendezVous", "doctor", "patient", "Diagnosis", "date", "url")

class RendezVousSerializer(serializers.ModelSerializer):
    consultation = ConsultationSerializer(many=True, read_only=True)
    doctor = DoctorSerializer(many=True, read_only=True)
    patient = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = RendezVous
        fields = ("id", "doctor", "patient", "Symptoms", "date", "consultation", "url")

class ReservationSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(many=True, read_only=True)
    patient = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ("id", "hotel", "patient", "fromDate", "toDate", "url")
    
