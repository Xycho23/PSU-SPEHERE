from django.db import models

class Locations(models.Model):
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.country

class FireStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('Minor', 'Minor'),
        ('Moderate', 'Moderate'),
        ('Major', 'Major'),
    ]
    
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    severity_level = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.severity_level} incident at {self.location} on {self.date_time}"

class FireIncident(models.Model):
    SEVERITY_CHOICES = [
        ('Minor', 'Minor'),
        ('Moderate', 'Moderate'),
        ('Major', 'Major'),
    ]
    
    date_time = models.DateTimeField(auto_now_add=True)
    severity_level = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'fire_incident'

    def __str__(self):
        return f"{self.severity_level} incident on {self.date_time}"
