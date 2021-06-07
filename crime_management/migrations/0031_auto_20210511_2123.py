# Generated by Django 3.2 on 2021-05-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0030_investigation_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation_report',
            name='legit_reason',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='investigation_report',
            name='legit_report',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=255, null=True),
        ),
    ]