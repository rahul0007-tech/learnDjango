from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello This is my home page") yesari pani return garna sakinxa
    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello This is my contact page")
    return render(request, 'contact.html')