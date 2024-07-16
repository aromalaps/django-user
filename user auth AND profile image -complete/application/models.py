from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profilepic=models.ImageField(upload_to='profilepics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
    phone=models.IntegerField()
    place=models.CharField(max_length=250)
    pincode=models.IntegerField()
    def __str__(self):
        return self.user
    