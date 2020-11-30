# Generated by Django 3.1.1 on 2020-11-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('middleName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('contactNumber', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=15)),
                ('availableBalance', models.IntegerField()),
                ('currentCashIn', models.IntegerField()),
            ],
            options={
                'db_table': 'Passenger',
            },
        ),
    ]
