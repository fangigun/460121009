from django.db import models

# Create your models here.
class Prices(models.Model):
    price_ID = models.IntegerField(primary_key = True)
    price_title = models.CharField(max_length=30) 
    price = models.CharField(max_length=10) 
    dahil1 = models.CharField(max_length=50)
    dahil2 = models.CharField(max_length=50) 
    dahil3 = models.CharField(max_length=50) 
    dahil4 = models.CharField(max_length=50) 
    dahil5 = models.CharField(max_length=50) 
    dahil6 = models.CharField(max_length=50)  
    dahil7 = models.CharField(max_length=50) 
    
    

    def __str__(self):
        return self.price_title
    

class Person(models.Model):
   
   Person_ID = models.IntegerField(primary_key = True)
   Name = models.CharField(max_length=20)
   LastName = models.CharField(max_length=20)  
   SignDate= models.DateField(auto_now_add=True)
   Person_Img=models.ImageField(upload_to='person',null=True,blank=True)

   def __str__(self):
        return self.LastName


class Student(models.Model):

    Student_ID = models.IntegerField(primary_key = True)
    Person_ID=models.ForeignKey(Person,on_delete=models.CASCADE)
    price_ID=models.ForeignKey(Prices,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CourseInstructor(models.Model):

    Instructor_ID = models.IntegerField(primary_key = True)
    Person_ID=models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Course(models.Model):

    Course_ID = models.IntegerField(primary_key = True)
    Course_title = models.CharField(max_length=30) 
    Course_Descp = models.CharField(max_length=250)
    Course_Img=models.ImageField(upload_to='course',null=True,blank=True)
    Instructor_ID=models.ForeignKey(CourseInstructor,on_delete=models.CASCADE)
    

   
    def __str__(self):
        return self.title


class Enrolment(models.Model):

    Enrolment_ID = models.IntegerField(primary_key = True)
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)
    Student_ID=models.ForeignKey(Student,on_delete=models.CASCADE)


    def __str__(self):
        return self.title    

     

    
        
