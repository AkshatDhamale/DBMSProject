# Generated by Django 3.2 on 2021-05-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0032_auto_20210512_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargesheet',
            name='report_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
