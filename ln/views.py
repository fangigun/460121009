from django.shortcuts import render
from ln.models import Prices

def index(request):

    return render(request, 'index.html') 

def courses(request):

    return render(request, 'courses.html')

def pricing(request):

    pricess=Prices.objects.all()
    return render(request, 'pricing.html',
         {'pricess':pricess})

def blog(request):

    return render(request, 'blog.html')

def contact(request):

    return render(request, 'contact.html')
    