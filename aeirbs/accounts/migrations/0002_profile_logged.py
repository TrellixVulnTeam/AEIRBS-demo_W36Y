# Generated by Django 2.2.6 on 2020-05-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='logged',
            field=models.BooleanField(default=False),
        ),
    ]
