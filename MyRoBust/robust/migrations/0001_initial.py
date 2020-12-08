# Generated by Django 3.1.1 on 2020-12-08 02:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('busID', models.AutoField(primary_key=True, serialize=False)),
                ('busName', models.CharField(max_length=50)),
                ('plateNumber', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('totalSeats', models.PositiveSmallIntegerField(default=51)),
                ('busFare', models.PositiveSmallIntegerField(default=0)),
                ('departureTime', models.TimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, null=True, upload_to='imagesBus/')),
            ],
            options={
                'db_table': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='DashboardBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalBuses', models.IntegerField()),
            ],
            options={
                'db_table': 'DashboardBus',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='imagesDriver/')),
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
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('date_booked', models.DateField(auto_now_add=True)),
                ('booking', models.AutoField(primary_key=True, serialize=False)),
                ('seatNumber', models.CharField(max_length=15)),
                ('dateReservation', models.DateField(default=django.utils.timezone.now)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robust.bus')),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]
