from django.urls import path
from . import views

urlpatterns = [
    path("", views.destination, name='destinations'),
    path('details/<int:destination_id>/', views.destination_detail, name='destination_detail')
]
