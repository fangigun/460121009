from django.forms import ModelForm,Textarea
from django import forms
from ln.models import Course



class CourseForm(ModelForm):
    Course_Descp= forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':4}))

    class Meta:
        model=Course
        fields='__all__'
        exclude=['user','Course_ID']