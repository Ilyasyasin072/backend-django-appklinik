"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.patient import views as views_patient
from api.doctor import views as views_doctor
from api.specialist import views as views_spesialist

router = routers.DefaultRouter()
router.register(r'patient', views_patient.PatientViewSet)
router.register(r'doctor', views_doctor.DoctorViewSet)
router.register(r'specialist', views_spesialist.SpecialistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls'))
]
