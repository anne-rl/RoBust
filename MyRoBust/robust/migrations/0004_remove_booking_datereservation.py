# Generated by Django 3.1.1 on 2020-12-08 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robust', '0003_auto_20201208_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='dateReservation',
        ),
    ]