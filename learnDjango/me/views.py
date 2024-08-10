from django.shortcuts import render

# Create your views here.

def first (request):
    return render(request, 'me/first.html')

def second (request):
    return render(request, 'me/second.html')