# Generated by Django 3.2 on 2021-05-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0046_auto_20210514_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminal',
            name='criminal_sentence_duration',
        ),
        migrations.AddField(
            model_name='criminal',
            name='jail_email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='criminal',
            name='jail_jailer',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='criminal',
            name='jail_phoneno',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
