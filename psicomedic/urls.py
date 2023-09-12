from django.contrib import admin
from django.urls import path
from .views import psychologists_view, psychologists_id_view,patients_view,patients_id_view,appointments_view,appointments_id_view


urlpatterns = [
    #Custom URLs
    path("psychologists/",psychologists_view),
    path("psychologists/<int:id>",psychologists_id_view),
    path("patients/", patients_view),
    path ("patients/<int:id>", patients_id_view),
    path("appointments/", appointments_view),
    path("appointments/<int:id>",appointments_id_view)
]