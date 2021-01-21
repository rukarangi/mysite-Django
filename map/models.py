from django.db import models

# Create your models here.

class PointFeature(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    zoom = models.FloatField(default=4)

    def __str__(self):
        return [self.latitude, self.longitude]