from django.db import models

from utils.models import Timestamps
# Create your models here.


class Certificate(Timestamps, models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
