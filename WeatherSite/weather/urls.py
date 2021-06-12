""" URLs for the Weather App. """
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index)
    ]
