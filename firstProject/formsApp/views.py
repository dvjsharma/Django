from django.shortcuts import render
from . import forms
from .models import Project
from .forms import ProjectForm
# Create your views here.
def userRegisterationView(request):
    form = forms.UserRegistrationForm()
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("First Name: " + form.cleaned_data['firstName']) #cleaned_data is a dictionary where everything will be stored
            print("Last Name: " + form.cleaned_data['lastName'])
            print("Email: " + form.cleaned_data['email'])
    return render(request, 'formsApp/userRegisteration.html', {'form': form})

def index(request):
    return render(request, 'formsApp/index.html')

def listProjects(request):
    projectList = Project.objects.all()
    return render(request, 'formsApp/listProjects.html', {'projects': projectList})

def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'formsApp/addProject.html', {'form': form})