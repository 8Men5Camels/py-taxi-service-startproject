from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=80)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self):
        return f"{self.model} ({self.manufacturer})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=40)

    class Meta:
        ordering = ["last_name"]
        constraints = [
            UniqueConstraint(
                fields=["license_number"], name="unique_license_number"
            )
        ]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name}) - {self.license_number}"