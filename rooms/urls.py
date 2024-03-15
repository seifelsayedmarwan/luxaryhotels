from django.urls import path
from . import views

urlpatterns = [
    # باقي المسارات هنا...
    path('room/<int:room_id>/', views.room_details, name='room_details'),
]
