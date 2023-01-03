from django.shortcuts import render
from ln.models import Prices
from ln.models import Course
from ln.models import Blog
from ln.models import Student
from ln.models import CourseInstructor
from ln.models import Testimonial
from accounts.decarator import allowed_users
def index(request):
    
    
    students=Student.objects.all()
    courses_s=Course.objects.all()
    inst=CourseInstructor.objects.all()
    toplam=0
    studentt=Student.objects.all()
    blogss=Blog.objects.all()[:3]
    for std in studentt:
        pricee=Prices.objects.get(pk=std.price_ID.pk)
        toplam+=pricee.price
    stu_count=0
    ins_count=0
    c_count=0
    for stu in students:
         stu_count+=1
    
    for ins in inst:
        ins_count+=1
        
    for cor in courses_s:
        c_count+=1   
    coursess=Course.objects.all()[:3]
    test=Testimonial.objects.all()
   
    return render(request, 'index.html'
    ,{'coursess':coursess,'stu_count':stu_count,'ins_count':ins_count,'c_count':c_count,'toplam':toplam,'blogss':blogss,'test':test})
    



def pricing(request):

   
    pricess=Prices.objects.all()
    
    return render(request, 'pricing.html',
         {'pricess':pricess})







    