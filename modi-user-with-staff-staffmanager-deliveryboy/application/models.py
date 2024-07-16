from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STAFF = 1
    STAFF_MANAGER = 2
    DELIVERY_BOY = 3
    
    FLAG_CHOICES = [
        (STAFF, 'Staff'),
        (STAFF_MANAGER, 'Staff Manager'),
        (DELIVERY_BOY, 'Delivery Boy'),
    ]
    
    flag = models.IntegerField(choices=FLAG_CHOICES, default=STAFF)
