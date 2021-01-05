from django.db import models
from datetime import date
import json

class Patient(models.Model):
    id:int=models.AutoField(primary_key=True)
    firstname:str=models.CharField(max_length=60)
    lastname:str=models.CharField(max_length=60)
    age:int=models.IntegerField()
    email:str=models.EmailField(max_length=254, unique=True)
    password:str=models.CharField(max_length=254)
    gender:str=models.CharField(max_length=6)
    address:str=models.CharField(max_length=60)
    phone:int=models.IntegerField()
    def __str__(self):
            return str(self.id)

class Doctor(models.Model):
    id:int=models.AutoField(primary_key=True)
    firstname:str=models.CharField(max_length=60)
    lastname:str=models.CharField(max_length=60)
    email:str= models.EmailField(max_length=254, unique=True)
    password:str=models.CharField(max_length=254)
    price:int=models.IntegerField()
    address:str=models.CharField(max_length=60)
    phone:int=models.IntegerField()
    speciality:str=models.CharField(max_length=60)
    def __str__(self):
        return str(self.id)
   

class Hotel(models.Model):
    id:int=models.AutoField(primary_key=True)
    name:str=models.CharField(max_length=60)
    email:str= models.EmailField(max_length=254, unique=True)
    password:str=models.CharField(max_length=254)
    address:str=models.CharField(max_length=60)
    phone:int=models.IntegerField()
    photo=models.ImageField(upload_to='app/uploads')
    price:int=models.IntegerField()
    def __str__(self):
            return str(self.id)
   
class RendezVous(models.Model):
    id:int=models.AutoField(primary_key=True)
    doctor:int=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="rendezvous")
    patient:int=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="rendezvous")
    Symptoms:str=models.CharField(max_length=60)
    date:date=models.DateField()
    def __str__(self):
            return str(self.id)
class Consultation(models.Model):
    id:int=models.AutoField(primary_key=True)
    rendezVous:int=models.ForeignKey(RendezVous, on_delete=models.CASCADE, related_name="consultation")
    doctor:int=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="consultations")
    patient:int=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="consultations")
    Diagnosis:str=models.CharField(max_length=60)
    date:date=models.DateField()
    def __str__(self):
            return str(self.id)
class Reservation(models.Model):
    id:int=models.AutoField(primary_key=True)
    hotel:int=models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reservations")
    patient:int=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="reservations")
    fromDate:date=models.DateField()
    toDate:date=models.DateField()
    def __str__(self):
            return str(self.id)
class TravelAgency(models.Model):
    id:int=models.AutoField(primary_key=True)
    travelAgencyName:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    addresse:str=models.CharField(max_length=60)
    phone:str =models.CharField(max_length=60)
    photo:str= models.ImageField(upload_to='app/uploads')
    price:str=models.IntegerField()
    def __str__(self):
            return str(self.id)
class MedicalCenter(models.Model):
    id:int=models.AutoField(primary_key=True)
    medicalCenterName:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    addresse:str=models.CharField(max_length=60)
    phone:str =models.CharField(max_length=60)
    photo:str= models.ImageField(upload_to='app/uploads')
    photo:str= models.ImageField(upload_to='app/uploads')
    price:str=models.IntegerField()
    def __str__(self):
            return str(self.id)