from django.db import models


class Arrivals(models.Model):
    day = models.CharField(max_length=255, default="N/A")
    date = models.DateField()
    time = models.CharField(max_length=255, default="N/A")
    flight = models.CharField(max_length=255, default="N/A")
    _from = models.CharField(max_length=255, default="N/A")
    airline = models.CharField(max_length=255, default="N/A")
    aircraft = models.CharField(max_length=255, default="N/A")
    status = models.CharField(max_length=255, default="Unknown")

    def __str__(self):
        return self.flight


class Depatures(models.Model):
    day = models.CharField(max_length=255, default="N/A")
    date = models.DateField()
    time = models.CharField(max_length=255, default="N/A")
    flight = models.CharField(max_length=255, default="N/A")
    destination = models.CharField(max_length=255, default="N/A")
    airline = models.CharField(max_length=255, default="N/A")
    aircraft = models.CharField(max_length=255, default="N/A")
    status = models.CharField(max_length=255, default="Unknown")
