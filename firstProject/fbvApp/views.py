from django.shortcuts import render, redirect
from fbvApp.models import Student
from fbvApp.forms import StudentForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def getStudent(request):
    students = Student.objects.all()
    return render(request, "fbvApp/students.html", {"students": students})

@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/index-fbv")
    return render(request, "fbvApp/createStudent.html", {"form": form})

@login_required
@permission_required("fbvApp.delete_student")
def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/index-fbv")

@login_required
def updateStudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/index-fbv")
    return render(request, "fbvApp/updateStudent.html", {"form": form})