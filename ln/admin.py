from django.contrib import admin
from ln.models import Prices
from ln.models import Student
from ln.models import CourseInstructor
from ln.models import Course
from ln.models import Enrolment
from ln.models import Blog
from ln.models import Testimonial

# Register your models here.
class TestiAdmin(admin.ModelAdmin):
    list_display= ["user"]


class PriceAdmin(admin.ModelAdmin):
    list_display= ["price_title"]
   
class StudentAdmin(admin.ModelAdmin):
    list_display= ["user"]


class InstructorAdmin(admin.ModelAdmin):
    list_display= ["user"]


class CourseAdmin(admin.ModelAdmin):
    list_display= ['Course_title']


class EnrollAdmin(admin.ModelAdmin):
    list_display= ["user"]

class BlogAdmin(admin.ModelAdmin):
    list_display= ["Blog_Title"]

class Meta:


    model=Prices
    model=Student
    model=CourseInstructor
    model=Course
    model=Enrolment
    model=Blog
    model=Testimonial



    admin.site.register(Prices,PriceAdmin)
    admin.site.register(Student,StudentAdmin)
    admin.site.register(CourseInstructor,InstructorAdmin)
    admin.site.register(Course,CourseAdmin)
    admin.site.register(Enrolment,EnrollAdmin)
    admin.site.register(Blog,BlogAdmin)
    admin.site.register(Testimonial,TestiAdmin)











