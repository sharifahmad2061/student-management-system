from django.db import models
from utils.models import Timestamps

# Create your models here.


class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    slides_url = models.URLField()
    lecturer_name = models.CharField(max_length=100, null=True, blank=True)
