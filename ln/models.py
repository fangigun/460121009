from django.db import models

# Create your models here.
class Price(models.Model):
    title = models.CharField(max_length=30) 
    price = models.CharField(max_length=10) 
    dahil1 = models.CharField(max_length=50)
    dahil2 = models.CharField(max_length=50) 
    dahil3 = models.CharField(max_length=50) 
    dahil4 = models.CharField(max_length=50) 
    dahil5 = models.CharField(max_length=50) 
    dahil6 = models.CharField(max_length=50)  
    dahil7 = models.CharField(max_length=50) 
    image=models.ImageField(upload_to=price,null=True,blank=True)

    def __str__(self):
        return self.title
    
