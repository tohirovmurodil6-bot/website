from django.contrib import admin
from .models import (
    Student, Teacher, School, Product, Customer,
    Employee, Deparment, Company, Manager, Director,
    Course, Lesson, Book, Author, Library, University,
    Faculty, Doctor, Patient, Hospital, Nurse, Pharmacy,
    Car, Driver, Taxi, Train
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'location')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name',)
    search_fields = ('first_name', 'last_name')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display=('name', 'location')
    search_fields=('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'age', 'location')
    list_filter=('location',)
    search_fields=('name', 'email')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'age', 'location')
    list_filter=('location',)
    search_fields=('name', 'email')


@admin.register(Deparment)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'location')
    search_fields=('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'location')
    search_fields=('name',)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name',)


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'location')
    search_fields=('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=('name', 'location', 'price', 'year')
    list_filter=('year',)
    search_fields=('name',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'location', 'price')
    search_fields=('name',)


@admin.register(Taxi)
class TaxiAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price')
    search_fields = ('name',)


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location')
    list_filter = ('location',)
    search_fields = ('name',)
