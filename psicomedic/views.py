from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from psicomedic.models import Psychologist, Patient, Appointment


# Create your views here.
def psychologists_view(request):
    psychologists = Psychologist.objects.all().values_list("first_name","last_name","email","phone")

    return HttpResponse(psychologists)

def psychologists_id_view(request, id):
    psychologists = Psychologist.objects.values(id).values_list("first_name","last_name","email","phone")

    return HttpResponse (psychologists)

def patients_view(request):
    patiens = Patient.objects.all().values_list("first_name","last_name","email","phone","biography")

    return HttpResponse (patiens)

def patients_id_view(request,user):
    return HttpResponse("patients_id_view")

def appointments_view(request):
    return HttpResponse("appointments_view")

def appointments_id_view(request,user):
    return HttpResponse("appointments_id_view")

