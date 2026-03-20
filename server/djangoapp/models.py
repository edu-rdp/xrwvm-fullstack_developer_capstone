from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[
        ('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon')
    ], default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )
    # Although not in the sample code, the instructions mention a Dealer ID
    dealer_id = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"