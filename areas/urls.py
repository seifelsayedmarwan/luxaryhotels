from  django.urls import path
from . import views

urlpatterns = [
    path('area/<int:area_id>/', views.area_detail, name='area_detail')
]
