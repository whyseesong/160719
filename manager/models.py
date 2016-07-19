import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

class User(models.Model):
    user_name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date published')
    def __str__(self):
        return self.user_name
    
    def was_published_recently(self):
        return self.join_date
        
    
class Device(models.Model):
    property_user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=200)
    device_confirm = models.BooleanField(default=False)
    def __str__(self):
        return self.device_name
# Create your models here.
