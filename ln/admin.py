from django.contrib import admin
from ln.models import Prices
from ln.models import Person
from ln.models import Student
from ln.models import CourseInstructor
from ln.models import Course
from ln.models import Enrolment
from ln.models import Blog

# Register your models here.

class PriceAdmin(admin.ModelAdmin):
    list_display= ["price_title"]
   


class PersonAdmin(admin.ModelAdmin):
    list_display= ["LastName"]


class StudentAdmin(admin.ModelAdmin):
    list_display= []


class InstructorAdmin(admin.ModelAdmin):
    list_display= ["Instructor_ID"]


class CourseAdmin(admin.ModelAdmin):
    list_display= ['Instructor_ID']


class EnrollAdmin(admin.ModelAdmin):
    list_display= []

class BlogAdmin(admin.ModelAdmin):
    list_display= ["Blog_Title"]

class Meta:


    model=Prices
    model=Person
    model=Student
    model=CourseInstructor
    model=Course
    model=Enrolment
    model=Blog



    admin.site.register(Prices,PriceAdmin)
    admin.site.register(Person,PersonAdmin)
    admin.site.register(Student,StudentAdmin)
    admin.site.register(CourseInstructor,InstructorAdmin)
    admin.site.register(Course,CourseAdmin)
    admin.site.register(Enrolment,EnrollAdmin)
    admin.site.register(Blog,BlogAdmin)











