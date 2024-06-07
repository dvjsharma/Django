from django.db import models

# Create your models here.
class Employee(models.Model): # employee class extends models.Model 
    firstName = models.CharField(max_length=30) #by defualt they are not null
    lastName = models.CharField(max_length=30) 
    salary = models.FloatField()
    email= models.CharField(max_length=30)
    
class Programmer(models.Model):
    name = models.CharField(max_length=30)
    salary = models.FloatField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    programmers = models.ManyToManyField(Programmer) # Many to many mapping (project => programmer we told, programmer => project django will take care)
    
class Customer(models.Model):
    name = models.CharField(max_length=30)
    
class PhoneNumber(models.Model):
    type = models.CharField(max_length=30)
    number = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # Many to one mapping (customer => phone number we told, phone number => customer django will take care, on deletion of customer delete phone number as well)
    
class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30) 
    age = models.IntegerField()
    
class License(models.Model):
    type = models.CharField(max_length=30) #by defualt they are not null
    validFrom = models.DateField() 
    validTo = models.DateField() 
    person = models.OneToOneField(Person, on_delete=models.CASCADE) # One to one mapping (person => license we told, license => person django will take care, on deletion of person delete license as well)
    