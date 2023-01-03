from django.shortcuts import render,redirect,get_object_or_404
from ln.models import CourseInstructor,Course,Enrolment
from django.contrib.auth.models import User,Group
from .forms import CourseForm
from accounts.decarator import allowed_users
from django.contrib.auth.decorators import login_required
@login_required(login_url='loginaccount')
def becomeinst(request):
    if request.method == 'POST':
        if request.user.groups.filter(name='Instructor').exists()==False:
            user=request.user
            group=Group.objects.get(name='Instructor')
            user.groups.add(group)
            CourseInstructor.objects.create(user=user,)
            return redirect('courses')
        else:
            return render(request,'becomeinstructor.html',{'error':'You are alerady a Instructor'})
    else:
        return render(request,'becomeinstructor.html')    

def courses(request):
    courses=Course.objects.all()
    return render(request, 'courses.html',
    {'coursess':courses})

@login_required(login_url='loginaccount')
@allowed_users(allowed_roles=['Instructor'])
def createcourse(request):
    if request.method =='GET':
        return render(request,'createcourse.html',{'form':CourseForm()})    
    else:
        try:
            form=CourseForm(request.POST,request.FILES)
            newCourse=form.save(commit=False)
            newCourse.user=request.user
            newCourse.save()
            return redirect('courses')
        except ValueError:
            return render(request,'createcourse.html',{'form':CourseForm(),'error':'bad data passed in'})            

def detail(request, Course_ID):
    course = get_object_or_404(Course,pk=Course_ID)
    if request.method == 'POST':
        user=request.user
        if user.student.price_ID==course.price_ID or user.student.price_ID_id==4 or course.price_ID_id==1 :       
            if  Enrolment.objects.filter(user=user,Course_ID=course).exists()==False:
                 Enrolment.objects.create(
                    user=user,Course_ID=course,
                )
            return redirect('courses')  
                  
        else:
    
    
            return render(request, 'coursedetail.html',{'course':course,'error':'Your package do not include this course'})        
    
    
    else:
        return render(request, 'coursedetail.html',{'course':course})


def usercourses(request):
    user=request.user
    usercor=Enrolment.objects.filter(user=user)
    return render(request, 'usercourses.html',{'usercor':usercor})



           

          
          
 
 
 

