from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

# Create your views here.
class GreetingView(View):
    def get(self, request):
        return HttpResponse("Hello Duniya")

class StudentListView(ListView):
    model = Student
    # default template name is student_list.html
    # default context name is student_list
    
class StudentDetailView(DetailView):
    model = Student
    # default template name is student_detail.html
    # default context name is student

class StudentCreateView(CreateView):
    model = Student
    fields = ["firstName", "lastName", "testScore"]
    # default template name is student_form.html
    # default context name is student_form
    
class StudentUpdateView(UpdateView):
    model = Student
    fields = ["testScore"]
    # default template name is student_form.html
    # default context name is student_form

class StudentDeleteView(DeleteView):
    model = Student
    # default template name is student_confirm_delete.html
    # default context name is student
    success_url = reverse_lazy("students")