from django.shortcuts import render
from django.http import HttpResponse # Add for request and respponse

# Create your views here.
def displayQuote(request):
    return HttpResponse("The best inverstment we can make is in our own abilities. - Roy T. Bennett ")