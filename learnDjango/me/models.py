from django.db import models
from django.utils import timezone

# Create your models here.

class Cars(models.Model):
    carTypes = [('SUV',"SUV"), ('sedan', "sedan")]
    name = models.CharField(max_length=30)
    carImg = models.ImageField(upload_to='cars/')
    registeredDate = models.DateTimeField(default=timezone.now)
    carType = models.CharField(max_length=15, choices=carTypes)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

