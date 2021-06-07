# Generated by Django 3.2 on 2021-05-08 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crime_management', '0011_auto_20210508_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'Person'), (2, 'Police'), (3, 'Admin')], default=3, max_length=10),
        ),
        migrations.AlterField(
            model_name='police',
            name='admin',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registerperson',
            name='admin',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]