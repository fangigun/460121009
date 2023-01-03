from django.http import HttpResponse
from django.shortcuts import redirect

def unaut_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request,*args,**kwargs)    
        

    return wrapper_func   

def allowed_users(allowed_roles=[]):
    def decarator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group= None
            if request.user.groups.filter(name='Instructor').exists():
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorized')
          
            

        return wrapper_func 
    return decarator

       