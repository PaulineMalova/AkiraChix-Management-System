from django.db import models

# Create your models here.
#Note the conventions
#CharField is a class inside the models thingie.
#max_length is not always required.
#Include this app in the settings.py file as part of the INSTALLED APPS - to make the app discoverable by django.
#This enables it to be converted into a database table.

# from .models import Student
# admin.site.register(Student)

#The two above are to be added to admin.py
class Student(models.Model) :  #Inheritance of attributes of another class. Model class in models.
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()  #Empty brackets because date formats are standard. No need for length declaration.
	gender = models.CharField(max_length = 20)
	registration_number = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 70)
	phone_number = models.CharField(max_length = 20)
	date_joined = models.DateField()

