from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=520)
    image=models.ImageField(upload_to="profile")
    phone=models.IntegerField()
    def __str__(self):
        return self.user

class Customer(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.username
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False