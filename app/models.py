from django.db import models
from datetime import date

class Patient(models.Model):
    id:int=models.AutoField(primary_key=True)
    firstname:str=models.CharField(max_length=60)
    lastname:str=models.CharField(max_length=60)
    age:int=models.IntegerField()
    email:str= models.EmailField(max_length=254)
    password:str=models.CharField(max_length=254)
    gender:str=models.CharField(max_length=1)
    address:str=models.CharField(max_length=60)
    phone:int=models.IntegerField()
    def __str__(self):
        return str(self.id)+","+self.firstname+","+self.lastname

class Doctor(models.Model):
    id:int=models.AutoField(primary_key=True)
    firstname:str=models.CharField(max_length=60)
    lastname:str=models.CharField(max_length=60)
    email:str= models.EmailField(max_length=254)
    password:str=models.CharField(max_length=254)
    price:int=models.IntegerField()
    address:str=models.CharField(max_length=60)
    phone:int=models.IntegerField()
    speciality:str=models.CharField(max_length=60)
    def __str__(self):
        return str(self.id)+","+self.firstname+","+self.lastname

class Hotel(models.Model):
    id:int=models.AutoField(primary_key=True)
    name:str=models.CharField(max_length=60)
    email:str= models.EmailField(max_length=254)
    password:str=models.CharField(max_length=254)
    address:str=models.CharField(max_length=60)
    phone:int=models.IntegerField()
    photo=models.ImageField(upload_to='app/uploads')
    price=models.IntegerField()

class RendezVous(models.Model):
    id:int=models.AutoField(primary_key=True)
    doctorId:int=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientId:int=models.ForeignKey(Patient, on_delete=models.CASCADE)
    Symptoms:str=models.CharField(max_length=60)
    date:date=models.DateField()

class Consultation(models.Model):
    id:int=models.AutoField(primary_key=True)
    rendezVousId:int=models.ForeignKey(RendezVous, on_delete=models.CASCADE)
    doctorId:int=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientId:int=models.ForeignKey(Patient, on_delete=models.CASCADE)
    Diagnosis:str=models.CharField(max_length=60)
    date:date=models.DateField()

class TravelAgency(models.Model):
    id:int=models.AutoField(primary_key=True)
    travelAgencyName:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    addresse:str=models.CharField(max_length=60)
    phone:str =models.CharField(max_length=60)
    photo:str= models.ImageField(upload_to='app/uploads')
    price:str=models.IntegerField()

class MedicalCenter(models.Model):
    id:int=models.AutoField(primary_key=True)
    medicalCenterName:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    addresse:str=models.CharField(max_length=60)
    phone:str =models.CharField(max_length=60)
    photo:str= models.ImageField(upload_to='app/uploads')
    photo:str= models.ImageField(upload_to='app/uploads')
    price:str=models.IntegerField()
