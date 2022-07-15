from django.shortcuts import render
from .models import Vehicle
from django.shortcuts import render, redirect
# from django.template import main



# Create your views here.

def car(request):
    vehicle = Vehicle.objects.all()
    context={'vehicle': vehicle}

    return render(request, 'index.html', context)