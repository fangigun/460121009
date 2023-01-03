from django.forms import ModelForm,Textarea
from django import forms
from ln.models import Student
from ln.models import Testimonial
class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        exclude=['user','price_ID']

class TestimonialForm(ModelForm):
    testimonial_message= forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':4}))
    class Meta:
        model=Testimonial
        fields='__all__'
        exclude=['user']