from django.db import models

# Create your models here.
class Crude(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='todoimage')
    message=models.TextField(max_length=250)
        
    def __str__(self):
        return self.name