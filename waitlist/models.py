from django.db import models
from utils.models import Timestamps
# Create your models here.


class Waitlist(Timestamps, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Waitlist'
