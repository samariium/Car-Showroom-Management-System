# Generated by Django 4.2.7 on 2023-11-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshowroom', '0008_car_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]