# Generated by Django 4.0.4 on 2022-05-29 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='location',
            name='slug',
        ),
    ]
