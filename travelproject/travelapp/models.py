# Create your models here.
from django.db import  models


class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descrip=models.TextField()

    def __int__(self):
        return self.name

class place1(models.Model):
    name1= models.CharField(max_length=250)
    img1= models.ImageField(upload_to='pics')
    descrip1= models.TextField()

    def __int__(self):
        return self.name1
