# Generated by Django 3.2.7 on 2021-12-16 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rede',
            name='dispositivos',
        ),
    ]