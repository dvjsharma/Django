from django.contrib import admin
from empApp.models import Employee
# Register your models here.

#! Only for showing selected fields, commenting as of now
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ["firstName", "lastName"]
# admin.site.register(Employee, EmployeeAdmin)

# to show all fields in admin page of the model
admin.site.register(Employee)

