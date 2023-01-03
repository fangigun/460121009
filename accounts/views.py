from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect,get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from .decarator import unaut_user
from ln.models import Student,Prices
from .forms import StudentForm
from .forms import TestimonialForm
from django.contrib.auth.decorators import login_required
def logoutaccount(request):
 logout(request)
 return redirect('index')

@unaut_user
def loginaccount(request):
   if request.method == 'GET':
      return render(request, 'loginaccount.html',{'form':AuthenticationForm})
   else:
      user = authenticate(request, username=request.POST['username'],password=request.POST['password']) 
      if user is None:
         return render(request,'loginaccount.html', {'form': AuthenticationForm(),'error': 'username and password donot match'})
      else:
         login(request,user)
         return redirect('index')
  

@unaut_user
def signup(request):
 if request.method == 'GET':
    return render(request, 'signup.html',
    {'form':UserCreationForm})

 else:
      if request.POST['password1'] ==request.POST['password2']:
         if len(request.POST['username']) >= 3 :
            if len(request.POST['password1']) >= 6 :
               try:     
                  user = User.objects.create_user(request.POST['username'],password= request.POST['password1'])
                  user.save()
                  group=Group.objects.get(name='Student')
                  user.groups.add(group)
                  Student.objects.create(
                     user=user,                 
                  )
                  login(request, user)
                  return redirect('index')            
               except IntegrityError:
                     return render(request,'signup.html',{'form':UserCreationForm,'error':'Username already taken. Choose new username.'})
            else:
                  return render(request,'signup.html',{'form':UserCreationForm,'error':'Your password have to be at least 6 characters.'})           
         else:
            return render(request,'signup.html',{'form':UserCreationForm,'error':'Username cant be empty. And has to be at least 3 characters'})
      else:
         return render(request, 'signup.html',
         {'form':UserCreationForm,'error':'Passwords do not match'})



@login_required(login_url='loginaccount')
def profile(request):
   student=request.user.student
   form=StudentForm(instance=student)
   if request.method == "POST":
      form=StudentForm(request.POST,request.FILES,instance=student)
      if form.is_valid():
         form.save()
   context={'form':form}
   return render(request, 'user_profile.html',context)

@login_required(login_url='loginaccount')
def testimonial(request):
   if request.method == 'GET':
        return render(request, 'testimonial.html',{'form':TestimonialForm()})
   else:
        try:
            form = TestimonialForm(request.POST,request.FILES)
            testimanial=form.save(commit=False)
            testimanial.user=request.user
            testimanial.save()
            return redirect('index')
        except ValueError:
            return render(request,'testimonial.html',{'form':TestimonialForm(),'error':'bad data passed in'})

@login_required(login_url='loginaccount')
def buyprice(request,Price_ID):
   price = get_object_or_404(Prices,pk=Price_ID)
   if request.method == 'POST':      
      Student.objects.filter(user=request.user).update(price_ID_id=price.pk)
      return redirect('pricing')

   else:
      return render(request,'price_buy.html')

              