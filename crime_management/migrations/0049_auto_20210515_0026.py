# Generated by Django 3.2 on 2021-05-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0048_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_image',
            field=models.FileField(blank=True, default=None, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='police',
            name='officer_image',
            field=models.FileField(blank=True, default=None, max_length=255, null=True, upload_to=''),
        ),
    ]