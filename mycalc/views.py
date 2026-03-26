from django.shortcuts import render

# Create your views here.
def calculate_view(request):
    return render (request, 'home.html')