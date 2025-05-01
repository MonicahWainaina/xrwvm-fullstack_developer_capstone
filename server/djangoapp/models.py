from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=50, default="Unknown")  # New field

    def __str__(self):
        return f"{self.name} ({self.country_of_origin})"  # Fixed line length


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023, validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )
    dealer = models.ForeignKey(
        'Dealer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # Fixed line length


# Dealer model
class Dealer(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name