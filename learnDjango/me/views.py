from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Cars

# Create your views here.

def first (request):
    cars = Cars.objects.all()
    return render(request, 'me/first.html',{'cars':cars})

def cardetails(request, car_id):
    car  = get_object_or_404(Cars, pk = car_id)
    return render(request, 'me/details.html',{'car':car})


def second (request):
    return render(request, 'me/second.html') 