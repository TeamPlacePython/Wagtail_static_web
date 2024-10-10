# Generated by Django 5.1.1 on 2024-10-09 13:35

import experience.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_experiencepage_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencepage',
            name='date_in',
            field=models.IntegerField(blank=True, null=True, validators=[experience.models.validate_year], verbose_name="Date d'entrée"),
        ),
        migrations.AddField(
            model_name='experiencepage',
            name='date_out',
            field=models.IntegerField(blank=True, null=True, validators=[experience.models.validate_year], verbose_name='Date de sortie'),
        ),
        migrations.AlterField(
            model_name='experiencepage',
            name='summary',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]