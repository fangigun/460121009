from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from .forms import ContactForm

def contact(request):

    if request.method == 'POST':
        form=ContactForm(request.POST)

        if form.is_valid():
            fname=form.cleaned_data['fname']
            print(fname)
            lname=form.cleaned_data['lname']
            name=fname+' '+lname
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            
            html=render_to_string('contactform.html/',{
                'name':name,
                'email':email,
                'message':message
            })
            send_mail(subject,message,email,['restorant.proje4@gmail.com'],html_message=html)
            return  redirect('contact')

    else:
        form=ContactForm() 
             

    return render(request, 'contact.html',{
        'form':form
    })
