from django.shortcuts import render
from ln.models import Prices
from ln.models import Course
from ln.models import Blog
from ln.models import Student
from ln.models import CourseInstructor

def index(request):
    students=Student.objects.all()
    coursess=Course.objects.all()
    inst=CourseInstructor.objects.all()
    toplam=0
    studentt=Student.objects.all()
    blogss=Blog.objects.all()[:3]
    for std in studentt:
        pricee=Prices.objects.get(price_ID=std.price_ID)
        toplam+=pricee.price
    stu_count=0
    ins_count=0
    c_count=0
    for stu in students:
         stu_count+=1
    
    for ins in inst:
        ins_count+=1
        
    for cor in coursess:
        c_count+=1   
    
    coursess=Course.objects.all()
    return render(request, 'index.html'
    ,{'coursess':courses,'stu_count':stu_count,'ins_count':ins_count,'c_count':c_count,'toplam':toplam,'blogss':blogss})
    

def courses(request):
    coursess=Course.objects.all()
    return render(request, 'courses.html',
    {'coursess':courses})

def pricing(request):

   
    pricess=Prices.objects.all()
    
    return render(request, 'pricing.html',
         {'pricess':pricess})

def blog(request):

    blogss=Blog.objects.all()
    return render(request, 'blog.html',
    {'blogss':blogss})

def contact(request):

    coursess=Course.objects.all()
    return render(request, 'contact.html')




    