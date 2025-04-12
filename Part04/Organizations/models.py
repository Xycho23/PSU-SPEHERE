from django.db import models

class organization(models.Model):  # Note: The class name should be singular
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name