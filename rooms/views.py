from django.shortcuts import render, get_object_or_404
from .models import Room

# Create your views here.

def room_details(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_details.html', {'room': room})
