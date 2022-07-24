from django.shortcuts import render
from .models import Vehicle
from django.shortcuts import render, redirect
from django.db.models import Q

# from django.template import main



# Create your views here.

def car(request):
    vehicle = Vehicle.objects.all()
    context={'vehicle': vehicle}

    return render(request, 'index.html', context)

def search(request):
    
    query = request.GET['q']

    search_results = Vehicle.objects.filter(
        Q(vehicleno__icontains=query) | Q(junction__icontains=query) | Q(location__icontains=query)
    )

    context = {
        'search_results': search_results,
        'query': query,
    }
    return render(request, 'search.html', context)