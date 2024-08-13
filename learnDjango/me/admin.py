from django.contrib import admin
from .models import Car, Booking, Review, Driver

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra=3

class CarAdmin(admin.ModelAdmin):
    list_display=('name','carType','description','registeredDate')
    inlines = [ReviewInline]

class BookingAdmin(admin.ModelAdmin):
    list_display=('bookingDate',)
    filter_horizontal = ('carBooking',)
    filter_horizontal = ('userBooking',)

class DriverAdmin(admin.ModelAdmin):
    list_display=('name','phone', 'registrationDate')

admin.site.register(Car, CarAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Driver, DriverAdmin)
