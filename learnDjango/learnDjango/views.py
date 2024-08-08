from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
    

def about(request):
    return HttpResponse("Hello This is my about page")

def contact(request):
    return HttpResponse("Hello This is my contact page")