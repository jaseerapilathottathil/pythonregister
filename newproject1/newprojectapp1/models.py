from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc =models.TextField()
class teacher(models.Model):
    name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics')
    qual = models.CharField(max_length=250)
    desg = models.TextField()

    def __str__(self):
           return self.name


