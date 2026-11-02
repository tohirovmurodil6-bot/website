from django.db import models
from auditlog.registry import auditlog


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Deparment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Company(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Manager(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Director(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Course(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Lesson(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
class Library(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
class University(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
class Faculty(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Patient(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Hospital(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Nurse(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Pharmacy(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Car(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    year=models.IntegerField()
    def __str__(self):
        return self.name
class Driver(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
class Taxi(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
class Train(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name



# Product modelidagi o'zgarishlarni kuzatish
auditlog.register(Product)

