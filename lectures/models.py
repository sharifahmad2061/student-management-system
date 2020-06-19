from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.models import Timestamps

# Create your models here.


class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(
        help_text='Enter number of hours', validators=[
            MinValueValidator(1), MaxValueValidator(10)])
    slides_url = models.URLField()
    is_required = models.BooleanField(default=False)
