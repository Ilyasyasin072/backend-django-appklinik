from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'patient/', views.PatientViewSet, basename='patient')

urlpatterns = [
    path('patient_list', views.PatientViewSet)
]