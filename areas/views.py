from django.shortcuts import render, get_object_or_404
from .models import Area
# Create your views here.
def area_detail(request, area_id):
    areas = get_object_or_404(Area, pk=area_id)
    hotels = areas.hotel_set.all()  # Fetch associated areas for the destination

    return render(request, 'area_details.html', {'areas': areas, 'hotels' : hotels})