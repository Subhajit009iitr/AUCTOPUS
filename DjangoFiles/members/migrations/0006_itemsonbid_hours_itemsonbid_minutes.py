# Generated by Django 4.1.3 on 2022-11-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_itemsonbid_initial_time_itemsonbid_time_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsonbid',
            name='hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemsonbid',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
    ]