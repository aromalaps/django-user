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