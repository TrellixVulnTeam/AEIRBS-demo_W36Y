# Generated by Django 2.2.6 on 2020-04-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0014_auto_20200419_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device_sensor',
            name='sensor_status',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.IntegerField(),
        ),
    ]
