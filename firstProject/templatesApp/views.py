from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    mydict = {
        "name": "Divij"
    }
    return render(request, 'templatesApp/firstTemplate.html', context=mydict)

def employee(request):
    mydict = {
        "id": 123,
        "name": "Divij",
        "sal" : 10000
    }
    return render(request, 'empApp/employees.html', context=mydict)
