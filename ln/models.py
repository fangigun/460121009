from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Prices(models.Model):
    
    price_title = models.CharField(max_length=30) 
    price =  models.IntegerField() 
    dahil1 = models.CharField(max_length=50)
    dahil2 = models.CharField(max_length=50) 
    dahil3 = models.CharField(max_length=50) 


    
    

    def __str__(self):
        return self.price_title
    

class Student(models.Model):

    user =models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=20,blank=True)
    LastName = models.CharField(max_length=20,blank=True)  
    SignDate= models.DateField(auto_now_add=True)
    Person_Img=models.ImageField(upload_to='person',null=True,blank=True,default="profile1.png")
    price_ID=models.ForeignKey(Prices,on_delete=models.CASCADE,blank=True,null=True,default=1)

   
    

    def __str__(self):
        return self.user.username




class CourseInstructor(models.Model):

    Instructor_ID = models.IntegerField(primary_key = True)
    user =models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Course(models.Model):

    Course_ID = models.IntegerField(primary_key = True)
    Course_title = models.CharField(max_length=30) 
    Course_Descp = models.CharField(max_length=250)
    Course_Img=models.ImageField(upload_to='course',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price_ID=models.ForeignKey(Prices,on_delete=models.CASCADE,blank=True,null=True,default=1)

   
    def __str__(self):
        return self.Course_title


class Enrolment(models.Model):

    Enrolment_ID = models.IntegerField(primary_key = True)
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username   



class Blog(models.Model):

    Blog_ID =  models.IntegerField(primary_key = True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    Blog_Title = models.CharField(max_length=50)
    Blog_Descp = models.CharField(max_length=250)
    Blog_Date= models.DateField(auto_now_add=True)
    Blog_Img=models.ImageField(upload_to='blog',null=True,blank=True)

    def __str__(self):
        return self.Blog_Title


class Testimonial(models.Model):

    user =models.ForeignKey(User,on_delete=models.CASCADE)
    testimonial_message=models.CharField( max_length=250)

    
        
