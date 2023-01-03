from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from ln.models import Blog
from django.http import HttpResponse
from blogs.forms import BlogForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

def detail(request, Blog_ID):
 blog = get_object_or_404(Blog,pk=Blog_ID)
 return render(request, 'blogdetail.html', 
 {'blog':blog})

@login_required(login_url='loginaccount')
def createblog(request):
    if request.method == 'GET':
        return render(request, 'createblog.html',{'form':BlogForm()})
    else:
        try:
            form = BlogForm(request.POST,request.FILES)

            newBlog=form.save(commit=False)
            newBlog.user=request.user
            newBlog.save()
            return redirect('blogs')
        except ValueError:
            return render(request,'createblog.html',{'form':BlogForm(),'error':'bad data passed in'})

def blogs(request):

    blogss=Blog.objects.all()
    return render(request, 'blog.html',
    {'blogss':blogss})
