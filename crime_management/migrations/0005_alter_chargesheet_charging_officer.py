# Generated by Django 3.2 on 2021-05-08 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0004_auto_20210508_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargesheet',
            name='charging_officer',
            field=models.CharField(default='username', max_length=255, null=True),
        ),
    ]
