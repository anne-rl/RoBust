# Generated by Django 3.1.1 on 2020-12-02 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('head', '0001_initial'),
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
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='head.bus')),
                ('seatNumber', models.CharField(max_length=15)),
                ('BusID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookingBusID', to='head.bus')),
            ],
            options={
                'db_table': 'Booking',
            },
            bases=('head.bus',),
        ),
    ]
