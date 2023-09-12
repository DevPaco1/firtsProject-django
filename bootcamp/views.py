from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def get_koder(request):
    #Response
    return HttpResponse("aqui tenemos todos los koders")

def list_koder(request):
    context = {
        "bootcamp": {"name": "Python", "module": "Django"},
        "koders": [
            {"name": "Benjamin", "generation": "1g", "bootcamp": "Python"},
            {"name": "Luis", "generation": "1g", "bootcamp": "Python"},
            {"name": "Irving", "generation": "1g", "bootcamp": "Python"},
        ],
    }

    # Creamos template
    template = loader.get_template("list_koders.html")

    return HttpResponse(template.render(context, request))

