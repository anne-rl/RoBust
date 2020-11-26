# Generated by Django 3.1.1 on 2020-11-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('emailAddress', models.CharField(max_length=50)),
                ('contactNumber', models.IntegerField()),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busName', models.CharField(max_length=50)),
                ('plateNumber', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('totalSeats', models.IntegerField()),
                ('busFare', models.FloatField()),
                ('departureTime', models.TimeField()),
                ('img', models.FileField(null=True, upload_to='media')),
            ],
            options={
                'db_table': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('emailAddress', models.CharField(max_length=50)),
                ('contactNumber', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Driver',
            },
        ),
    ]
