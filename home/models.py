from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    

    def __str__(self):
        return self.name
class Admission_Form(models.Model):
    name=models.CharField(max_length=122)
    fname=models.CharField(max_length=122)
    mname=models.CharField(max_length=122)
    gender=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    add=models.CharField(max_length=122)
    


    def __str__(self):
        return self.name
    

    