from django.db import models
from datetime import date
# Create your models here.


    

class  Patient(models.Model):
    id:int=models.AutoField(primary_key=True)
    userName:str=models.CharField(max_length=60)
    age:int=models.IntegerField()
    email:str= models.EmailField(max_length=254)
    password:str=models.CharField(max_length=254)
    gender:str=models.CharField(max_length=1)
    jobTitle:str=models.CharField(max_length=60)
    bodyGroup:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    DiseaseDescription:str=models.CharField(max_length=60)
    phone:str=models.CharField(max_length=60)
    def __str__(self):
        return str(self.id)+","+self.userName

class Doctor(models.Model):
    id:int=models.AutoField(primary_key=True)
    userName:str=models.CharField(max_length=60)
    age:int=models.IntegerField()
    email:str= models.EmailField(max_length=254)
    password:str=models.CharField(max_length=254)
    price:int=models.IntegerField()
    jobTitle:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    addresse:str=models.CharField(max_length=60)
    phone:str =models.CharField(max_length=60)
    speciality:str=models.CharField(max_length=60)

    def __str__(self):
            return str(self.id)+","+self.userName

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



class Hotel(models.Model):
    id:int=models.AutoField(primary_key=True)
    hotelName:str=models.CharField(max_length=60)
    city:str=models.CharField(max_length=60)
    addresse:str=models.CharField(max_length=60)
    phone:str =models.CharField(max_length=60)
    photo = models.ImageField(upload_to='app/uploads')
    price=models.IntegerField()

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
