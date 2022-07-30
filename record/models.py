import email
from email.mime import image
from unicodedata import name
from django.db import models
from django.forms import ImageField

# Create your models here.
class Student(models.Model):
    gender_list={
        ('male','Male'),
        ('female','Female'),
    }
    language_list={
        ('nepali','Nepali'),
        ('chinese','Chinese'),
        ('english','English'),
    }
    country_list={
        ('nepal','Nepal'),
        ('china','China'),
        ('usa','USA'),
    }
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    gender=models.CharField(choices=gender_list, max_length=6)
    address=models.CharField(max_length=255)
    phone=models.IntegerField()
    language=models.CharField(choices=language_list, max_length=50)
    country=models.CharField(choices=country_list, max_length=10)
    image=models.ImageField(upload_to='students',blank=True,null=True)


    def get_language(self):
        return self.language.split(',')