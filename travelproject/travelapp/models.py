# Create your models here.
from django.db import models


class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descrip=models.TextField()

    def __int__(self):
        return self.name
