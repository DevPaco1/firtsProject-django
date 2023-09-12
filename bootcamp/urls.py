from django.contrib import admin
from django.urls import path
from .views import get_koder,list_koder

urlpatterns = [
    #Custom URLs
    path("koders",list_koder),
    path("koders/id",get_koder),
]
