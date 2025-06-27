from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car  # Make sure this import matches your actual model

def index(request):
    cars = Car.objects.all()  # ✅ This line defines 'cars'
    return render(request, 'index.html', {'cars': cars})  # ✅ Now this will work


# Create your views here.



































