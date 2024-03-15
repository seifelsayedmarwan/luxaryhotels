from django.urls import path
from . import views

urlpatterns = [
    # باقي المسارات هنا...
    path('hotel/<int:hotel_id>/', views.hotel_details, name='hotel_details'),
]
