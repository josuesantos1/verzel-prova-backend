from django.db import models

class Vehicles(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    brand = models.CharField(
        max_length=32,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=10240,
    )

    price = models.IntegerField()

    sold = models.BooleanField(
        default=False
    ) 
    

class VehiclesImages(models.Model):
    vehicles = models.ForeignKey(
        Vehicles, on_delete=models.CASCADE
    )

    key = models.CharField(
        max_length=64,
        null=False,
        blank=False
    )
