# Generated by Django 4.2.4 on 2023-09-25 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
