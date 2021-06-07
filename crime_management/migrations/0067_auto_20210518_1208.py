# Generated by Django 3.2 on 2021-05-18 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0066_meeting_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyCheckup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('criminal_id', models.IntegerField(blank=True, default=None, null=True)),
                ('criminal_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('jail_id', models.IntegerField(blank=True, default=None, null=True)),
                ('doctor_id', models.IntegerField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.IntegerField(blank=True, default=0, null=True)),
                ('BMI', models.IntegerField(blank=True, default=0, null=True)),
                ('BP', models.IntegerField(blank=True, default=0, null=True)),
                ('Hearing', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Vision', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Dental', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('MentalHealth', models.TextField(blank=True, default=None, null=True)),
                ('Injuries', models.TextField(blank=True, default=None, null=True)),
                ('Medications', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_room',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]