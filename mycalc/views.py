from django.shortcuts import render

# Create your views here.
def calculate_view(request):
    return render (request, 'calculator/index.html')