# Generated by Django 3.2 on 2021-05-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0068_auto_20210518_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='reject_reason',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
