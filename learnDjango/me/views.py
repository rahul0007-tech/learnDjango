from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Car, User
from . forms import RgistarionForm

# Create your views here.

def first (request):
    cars = Car.objects.all()
    return render(request, 'me/first.html',{'cars':cars})

def cardetails(request, car_id):
    car  = get_object_or_404(Car, pk = car_id)
    return render(request, 'me/details.html',{'car':car})


def second (request):
    return render(request, 'me/second.html') 

def signup(request):
    if request.method == "POST":
        form = RgistarionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['firstName']
            last_name = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create the user
            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
    else:
        form= RgistarionForm()
    return render(request, 'me/signup.html',{'form':form})