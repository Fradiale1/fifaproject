# fifas/models.py

from django import models


class Airline(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.model


class fifa(models.Model):
    fifa_number = models.CharField(max_length=255)
    airline = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateField()

    def __str__(self):
        return self.fifa_number
