# Generated by Django 3.2 on 2021-05-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0036_auto_20210512_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargesheet',
            name='Informant_email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
