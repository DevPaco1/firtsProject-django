"""
URL configuration for firstProyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import bienvenida, despedida, saludo, saludar_con_nombre,mentor_koder, type_and_name


urlpatterns = [
    #Custom URLs
    path("",bienvenida),
    path("despedida",despedida),
    path("saludo", saludo),
    path ("saludo/<str:nombre>", saludar_con_nombre),
    path("kodemia/<str:user>", mentor_koder),
    path("user/<str:type>/<str:name>",type_and_name)
]
