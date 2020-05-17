from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

    class Meta:
    	verbose_name_plural = "airport"
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    def is_valid_flight(self):
        return (self.origin != self.destination)

    def __str__(self):
    	return f"{self.id} - {self.origin} to {self.destination}"

    class Meta:
    	verbose_name_plural = "flight"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

    class Meta:
    	verbose_name_plural = "passenger"
    	    