from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='requisition/%Y/%m/%d/', blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    staff_id = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
