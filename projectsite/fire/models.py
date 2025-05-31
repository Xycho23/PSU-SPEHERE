from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class FireStation(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Incident(models.Model):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    
    def __str__(self):
        return f"Incident at {self.location} on {self.date}"
