from django.shortcuts import render



def index(request):

    return render(request, 'index.html') 

def courses(request):

    return render(request, 'courses.html')

def pricing(request):

    return render(request, 'pricing.html')

def blog(request):

    return render(request, 'blog.html')

def contact(request):

    return render(request, 'contact.html')
    