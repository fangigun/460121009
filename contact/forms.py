from django import forms

class ContactForm(forms.Form):
    fname=forms.CharField(max_length=100)
    lname=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=600)

