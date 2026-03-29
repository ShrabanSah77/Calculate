from django.urls import path
from django.http import HttpResponse
from mycalc.views import *

urlpatterns = [
    path('', calculate_view, name = 'calculate_view'),
]