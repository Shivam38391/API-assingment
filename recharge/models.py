from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # add additional fields if needed
    pass

class Planes(models.Model):
    
    name = models.CharField(max_length=20)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    operator = models.CharField(max_length=50)
    validity = models.DurationField()
    description = models.CharField(max_length=255)
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Recharg(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_plan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    circle = models.CharField( max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    

    def __str__(self):
        return self.user.username


