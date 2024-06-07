from django.shortcuts import render
from django.http import HttpResponse # Add for request and respponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>My First Django App!! </h1>")

def displayDateTime(request):
    currentDt = datetime.datetime.now()
    s= "<h1>Current Date and Time is: "+str(currentDt)+"</h1>"
    return HttpResponse(s) # only accepts string