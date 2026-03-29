from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your own views here.

def calculate_view(request):
    if request.method == 'POST':
        result = request.POST.get('result', '')

        return render(request, 'calculate/index.html', {'result': result})
    return render(request, 'calculate/index.html')
