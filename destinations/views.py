# views.py in destinations app
from django.shortcuts import render, get_object_or_404
from .models import Destination

def destination(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})

def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    areas = destination.area_set.all()  # Fetch associated areas for the destination

    return render(request, 'details.html', {'destination': destination, 'areas': areas})
