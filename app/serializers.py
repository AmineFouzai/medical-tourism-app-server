from rest_framework import serializers
from .models import (Patient,Doctor,Consultation,RendezVous,Hotel,TravelAgency,MedicalCenter,Reservation)

class RendezVousPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id","firstname","lastname","age","email","gender","address","phone","url")


class RendezVousDoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = ("id","firstname","lastname","email","address","phone","speciality","price","url")

class RendezVousSerializer(serializers.ModelSerializer):
    
    # doctor=RendezVousDoctorSerializer(many=False,read_only=True) 
    # patient=RendezVousPatientSerializer(many=False,read_only=True) 
    class Meta:
        model = RendezVous
        fields = ("id", "doctor", "patient","Symptoms", "date", "consultation", "url")

class PaitentRendezVousSerializer(serializers.ModelSerializer):
    doctor=RendezVousDoctorSerializer(many=False,read_only=True)
    class Meta:
        model = RendezVous
        fields = ("id", "doctor", "patient","Symptoms", "date", "consultation", "url")

class DoctorRendezVousSerializer(serializers.ModelSerializer):
    patient=RendezVousPatientSerializer(many=False,read_only=True)
    class Meta:
        model = RendezVous
        fields = ("id", "doctor", "patient","Symptoms", "date", "consultation", "url")

#######################################################################################
#######################################################################################

        
class ConsultationSerializer(serializers.ModelSerializer):
    # rendezVous=RendezVousSerializer(many=False,read_only=True)
    class Meta:
        model = Consultation
        fields = ("id", "rendezVous", "doctor", "patient", "Diagnosis", "date", "url")




#######################################################################################
#######################################################################################

class ReservationPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id","firstname","lastname","age","email","gender","address","phone","url")

class ReservationHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id","name","address","email","password","phone","photo","price","url","reservations")

 

class ReservationSerializer(serializers.ModelSerializer):
    # patient=ReservationPatientSerializer(many=False,read_only=False)
    # hotel=ReservationHotelSerializer(many=False,read_only=False)

    class Meta:
        model = Reservation
        fields = ("id", "hotel", "patient", "fromDate", "toDate", "url")
    


#######################################################################################
#######################################################################################

class PatientSerializer(serializers.ModelSerializer):

    rendezvous = PaitentRendezVousSerializer(many=True, read_only=True)
    consultations = ConsultationSerializer(many=True, read_only=True)
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ("id","firstname","lastname","age","email","password","gender","address","phone","url","rendezvous","consultations","reservations")


class DoctorSerializer(serializers.ModelSerializer):
    rendezvous = DoctorRendezVousSerializer(many=True, read_only=True)
    consultations = ConsultationSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ("id","firstname","lastname","email","password","address","phone","speciality","price","url","rendezvous","consultations")

class HotelSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ("id","name","address","email","password","phone","photo","price","url","reservations")

