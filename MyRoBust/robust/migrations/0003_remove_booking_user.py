# Generated by Django 3.1.1 on 2020-12-08 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robust', '0002_auto_20201208_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
