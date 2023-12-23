from django.db import models

# Create your models here.
class Jobapplication(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image')
    resume=models.FileField(upload_to='resume file')
