from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=250, null=True, blank=True)
    job = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True, )

    def __str__(self):
        return str(self.user)

class Student(models.Model):
    roll_no = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.roll_no)




