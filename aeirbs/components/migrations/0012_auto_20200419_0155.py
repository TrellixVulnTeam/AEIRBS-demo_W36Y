# Generated by Django 2.2.6 on 2020-04-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0011_auto_20200418_1853'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Component',
        ),
        migrations.RemoveField(
            model_name='device_sensor',
            name='floor_location',
        ),
        migrations.AlterField(
            model_name='device',
            name='device_status',
            field=models.IntegerField(choices=[(0, 'Connected'), (1, 'Inactive'), (2, 'Under Maintenance'), (3, 'Needs Maintenance')], default=0),
        ),
        migrations.AlterField(
            model_name='device_sensor',
            name='sensor_status',
            field=models.IntegerField(choices=[(0, 'Connected'), (1, 'Inactive'), (2, 'Under Maintenance'), (3, 'Needs Maintenance')], default=0),
        ),
        migrations.DeleteModel(
            name='ComponentConnection',
        ),
    ]
