# Generated by Django 2.2.6 on 2020-04-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20200211_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_status',
            field=models.IntegerField(choices=[(1, 'Connected'), (2, 'Inactive'), (3, 'Under Maintenance'), (4, 'Needs Maintenance')]),
        ),
        migrations.AlterField(
            model_name='device',
            name='floor_location',
            field=models.IntegerField(choices=[(1, 'First Floor'), (2, 'Second Floor'), (3, 'Third Floor'), (4, 'Fourth Floor')], default=1),
        ),
    ]
