from django.urls import include, path
from rest_framework import routers
from .views import (PatientViewSet,DoctortViewSet,HotelViewSet,login)
from django.conf.urls.static import static
import os 

PATH = '/app/uploads/'
ROOT = os.getcwd()+"/app/uploads/"
router = routers.DefaultRouter()
router.register(r'patient', PatientViewSet)
router.register(r'doctor', DoctortViewSet)
router.register(r'hotel', HotelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/',login)
    
]+static(PATH, document_root=ROOT)
