from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)    
    phonenumber = models.CharField(max_length=13)
    address = models.CharField(max_length=350)
    def __str__(self):
        return self.phonenumber
