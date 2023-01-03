from django.forms import ModelForm,Textarea
from django import forms
from ln.models import Blog

class BlogForm(ModelForm):
   

    class Meta:
        model=Blog
        fields=['Blog_Title','Blog_Descp','Blog_Img']
        