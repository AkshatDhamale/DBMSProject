# Generated by Django 3.2 on 2021-05-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0071_report_person_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='person_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
