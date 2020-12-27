from django.contrib import admin
from .models import (Patient,Doctor,Consultation,RendezVous,Hotel,TravelAgency,MedicalCenter)

# Register your models here.
admin.site.register(Patient) 
admin.site.register(Doctor) 
admin.site.register(RendezVous) 
admin.site.register(Consultation) 
admin.site.register(Hotel) 
admin.site.register(TravelAgency) 
admin.site.register(MedicalCenter) 
