from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    carTypes = [('SUV',"SUV"), ('sedan', "sedan")]
    name = models.CharField(max_length=30)
    carImg = models.ImageField(upload_to='cars/')
    registeredDate = models.DateTimeField(default=timezone.now)
    carType = models.CharField(max_length=15, choices=carTypes)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    # One to One Relation
class Driver(models.Model):
    relation = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='drivers')
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    registrationDate = models.DateField(default=timezone.now)

    def __str__(self):
	    return self.name


    # One To Many Relation
class Review(models.Model):
    relation = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comment= models.TextField()
    reviewDate=models.DateField(default=timezone.now)

    def __str__(self):
	    return f'{self.user.username} review for {self.relation.name}'
    

    # Many To Many Relation
class Booking(models.Model):
     bookingDate = models.DateField(default=timezone.now)
     carBooking = models.ManyToManyField(Car, related_name='bookings')
     userBooking = models.ManyToManyField(User, related_name='bookings')





