from django.shortcuts import render, get_object_or_404
from .models import Hotel

def hotel(request):
    hotels = hotel.objects.all()
    return render(request, 'hotel_details.html', {'hotels': hotels})

def hotel_details(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = hotel.room_set.all()
    return render(request, 'hotel_details.html', {'hotel': hotel, 'rooms' : rooms})
