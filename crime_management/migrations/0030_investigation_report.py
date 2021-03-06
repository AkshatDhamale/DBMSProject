# Generated by Django 3.2 on 2021-05-11 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0029_theories_report_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigation_Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_id', models.IntegerField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('scene_address', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('scene_firstvisited', models.DateTimeField(default=None)),
                ('scene_description', models.TextField(blank=True, default=None, null=True)),
                ('main_witness_name', models.CharField(max_length=255)),
                ('main_witness_email', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('main_witness_address', models.CharField(max_length=255)),
                ('main_witness_phone_no', models.CharField(max_length=15)),
                ('main_witness_DOB', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('main_witness_description', models.TextField(blank=True, default=None, null=True)),
                ('main_witness_blame', models.TextField(blank=True, default=None, max_length=255, null=True)),
                ('main_suspect_name', models.CharField(max_length=255)),
                ('main_suspect_email', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('main_suspect_address', models.CharField(max_length=255)),
                ('main_suspect_phone_no', models.CharField(max_length=15)),
                ('main_suspect_DOB', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('main_suspect_description', models.TextField(blank=True, default=None, null=True)),
                ('main_suspect_defense', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
