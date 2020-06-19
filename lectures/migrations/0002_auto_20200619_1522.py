# Generated by Django 3.0.7 on 2020-06-19 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1, help_text='Enter number of hours', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
    ]
