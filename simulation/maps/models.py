from django.db import models
from django.contrib.postgres.fields import ArrayField


class simulationModel(models.Model):
    sratLocs = models.JSONField()
    peopleCount = models.FloatField(default=0)
    endLocs = models.JSONField()
    endCapacity = models.FloatField(default=0)
    emergencyLocs = models.JSONField()
    emergencyCapacity = models.FloatField(default=0)
    dangerLocs = models.JSONField()
    dangerPossibility = models.FloatField(default=0)



