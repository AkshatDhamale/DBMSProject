# Generated by Django 3.2 on 2021-05-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0055_alter_work_work_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='status_work',
            field=models.CharField(blank=True, choices=[('Alloted', 'Alloted'), ('Not_Alloted', 'Not_Alloted')], default='Not_Alloted', max_length=255, null=True),
        ),
    ]
