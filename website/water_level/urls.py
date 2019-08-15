from django.urls import path
from . import views

app_name = 'water_level'
urlpatterns = [
    path('', views.karnataka_map, name='karnataka_map'),
]