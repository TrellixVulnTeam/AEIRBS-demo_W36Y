# Generated by Django 2.2.6 on 2020-05-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.IntegerField(choices=[(0, 'Earthquake'), (1, 'Fire'), (2, 'Flood')]),
        ),
    ]
