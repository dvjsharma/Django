from django.shortcuts import render
from empApp.models import Employee
# Create your views here.

def emploteedata(request):
    emploteedata = Employee.objects.all()
    empDict = {
        "employees": emploteedata
    }
    return render(request, 'empApp/employees.html', context=empDict)